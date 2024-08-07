import random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import logging


class Main_info(APIView):
    def get(self, request, tg_id: int, name: str):
        try:
            player = Player.objects.get(tg_id=tg_id)
        except Player.DoesNotExist:
            player = Player.objects.create(tg_id=tg_id, name=name)
            Upgrade.objects.create(player=player)

        info = {"lvl": player.lvl,
                "coin": player.coin,
                "energy_start": player.energy,
                "energy_now": player.now_energy,
                "crystal": player.crystal,
                "flag_autobot": player.upgrade.flag_autobot,
                "timer_autobot": player.upgrade.autobot_time,
                "money_per_tap": player.upgrade.damage,
                "energy_per_tap": player.upgrade.one_tap_energy,
                "coin_bonus_result": player.upgrade.coin_bonus_result}

        return Response(info, status=status.HTTP_200_OK)


class Tap_Tap(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=request.data['tg_id'])
        coin = int(self.request.data['coin'])
        energy = int(self.request.data['energy_now'])
        player.coin += coin
        player.now_energy = energy
        player.save(update_fields=['now_energy', 'coin'])
        return Response({"coin": player.coin, "energy_now": player.now_energy}, status=status.HTTP_200_OK)


class Autobot(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=self.request.data['tg_id'])
        upgrade = get_object_or_404(Upgrade, player=player)
        upgrade.flag_autobot = False
        upgrade.save(update_fields=['flag_autobot'])
        return Response({"timer": upgrade.autobot_time, "flag_autobot": upgrade.flag_autobot},
                        status=status.HTTP_200_OK)


class Take_Bonus_Autobot(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=request.data['tg_id'])
        if player.upgrade.coin_bonus_result != 0 and player.upgrade.flag_autobot == True:
            player.coin += player.upgrade.coin_bonus_result
            player.upgrade.coin_bonus_result = 0
            player.upgrade.autobot_time = player.upgrade.start_autobot_time
            player.save()
            player.upgrade.save()
            return Response({"Success": "Деньги добавлены"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error": "Нечего забирать"}, status=status.HTTP_425_TOO_EARLY)


class Info_Upgrade(APIView):
    def get(self, request, tg_id: int):
        player = get_object_or_404(Player, tg_id=tg_id)
        data = {"energy": player.energy,
                "energy_lvl": player.upgrade.energy_lvl,
                "price_lvl_up_energy": player.upgrade.price_lvl_up_energy,
                "damage": player.upgrade.damage,
                "price_lvl_up_damage_and_energy": player.upgrade.price_lvl_up_damage_and_energy,
                "lvl_one_tap_damage_and_energy": player.upgrade.lvl_one_tap_damage_and_energy}
        return Response(data, status=status.HTTP_200_OK)


class UpgradeEnergy(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=self.request.data['tg_id'])
        if player.coin >= player.upgrade.price_lvl_up_energy:
            player.coin -= player.upgrade.price_lvl_up_energy
            player.energy += 500
            player.upgrade.energy_lvl += 1
            player.upgrade.price_lvl_up_energy *= 2
            player.save()
            player.upgrade.save()
            return Response({"coin": player.coin,
                             "energy_lvl": player.upgrade.energy_lvl,
                             "price_lvl_up_energy": player.upgrade.price_lvl_up_energy, }, status=status.HTTP_200_OK)

        else:
            return Response({"Error": "Недостаточно денег!"}, status=status.HTTP_400_BAD_REQUEST)


class UpgradeDamage(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=self.request.data['tg_id'])
        if player.coin >= player.upgrade.price_lvl_up_damage_and_energy:
            player.coin -= player.upgrade.price_lvl_up_damage_and_energy
            player.upgrade.damage += 1
            player.upgrade.one_tap_energy += 1
            player.upgrade.lvl_one_tap_damage_and_energy += 1
            player.upgrade.price_lvl_up_damage_and_energy *= 2
            player.save()
            player.upgrade.save()
            return Response({"coin": player.coin,
                             "damage": player.upgrade.damage,
                             "one_tap_energy": player.upgrade.one_tap_energy,
                             "lvl_one_tap_damage_and_energy": player.upgrade.lvl_one_tap_damage_and_energy,
                             "price_lvl_up_damage_and_energy": player.upgrade.price_lvl_up_damage_and_energy},
                            status=status.HTTP_200_OK)

        else:
            return Response({"Error": "Недостаточно денег!"}, status=status.HTTP_400_BAD_REQUEST)


class Get_All_Box(APIView):
    def get(self, request):
        boxes = Box.objects.all()
        response_data = []
        for box in boxes:
            box_data = {
                'name': box.name,
                'prizes': []
            }
            for prize in box.prizes.all():
                prize_data = {
                    'prize_name': prize.name,
                    'prize_count': prize.count,
                    'prize_chance': prize.chance
                }
                box_data['prizes'].append(prize_data)
            response_data.append(box_data)
        return Response(response_data)


class Open_Box(APIView):
    def post(self, request):
        name = request.data['name_box']
        box = get_object_or_404(Box, name=name)
        prize_count = {'Bronze': 1, 'Silver': 2, 'Gold': 3}.get(name, 0)
        prizes = box.prizes.all()
        result = []
        for _ in range(prize_count):
            rand = random.uniform(0, 100)
            summ_chance = 0
            for prize in prizes:
                summ_chance += prize.chance
                if rand <= summ_chance:
                    result.append({
                        'prize_name': prize.name,
                        'prize_count': prize.count,
                        'prize_chance': prize.chance
                    })
                    break

        return Response(result)


class Take_And_Apply_Bonus(APIView):
    def post(self, request):
        player = get_object_or_404(Player, tg_id=request.data['tg_id'])
        prizes = request.data.get('prizes', [])

        for prize in prizes:
            prize_name = prize.get('prize_name')
            prize_count = prize.get('prize_count', 1)  # Значение по умолчанию 1

            if prize_name == "Coin Boosts":
                player.upgrade.damage += 1
                player.upgrade.one_tap_energy += 1
                player.upgrade.lvl_one_tap_damage_and_energy += 1
                player.upgrade.price_lvl_up_damage_and_energy *= 2
            elif prize_name == "Energy Boosts":
                if player.now_energy == player.energy:
                    player.now_energy += 500
                player.energy += 500
                player.upgrade.energy_lvl += 1
                player.upgrade.price_lvl_up_energy *= 2
            elif prize_name == "Bot Boosts":
                if player.upgrade.autobot_time == player.upgrade.start_autobot_time:
                    player.upgrade.autobot_time += 300
                player.upgrade.start_autobot_time += 300
                player.upgrade.autobot_lvl += 1
            elif prize_name == "Dimonds":
                player.crystal += prize_count
                a = {'key': 'вам выпал скин'}

        player.save()
        player.upgrade.save()
        return Response({'Success': 'Бонусы получены '})


class CompleteReferralSystem(APIView):
    def get(self, request, new_id: int, referral_id: int):
        if new_id == referral_id:
            return Response({"Error": "Нельзя добавить самого себя в друзья!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            new_person = get_object_or_404(Player, tg_id=new_id)
            referral = get_object_or_404(Player, tg_id=referral_id)

            info1_exists = ReferralSystem.objects.filter(referral=referral, new_person=new_person).exists()
            info2_exists = ReferralSystem.objects.filter(referral=new_person, new_person=referral).exists()

            if info1_exists or info2_exists:
                return Response({"Error": "Данной игрок уже находится у вас в друзьях"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                ReferralSystem.objects.create(referral=referral, new_person=new_person)
                return Response({'success': 'Перейдите во кладку друзья и заберите бонус'}, status=status.HTTP_200_OK)


class AllFriends(APIView):
    def get(self, request, tg_id: int):
        person = get_object_or_404(Player, tg_id=tg_id)
        data = []
        info = ReferralSystem.objects.filter(referral=person)
        if info:
            for i in info:
                data.append({'name': i.new_person.name,
                             'lvl': i.new_person.lvl,
                             'player_id': i.new_person.id,
                             'referral_system_id': i.id,
                             'flag': i.new_person_bonus})

        info = ReferralSystem.objects.filter(new_person=person)
        if info:
            for i in info:
                data.append({'name': i.referral.name,
                             'lvl': i.referral.lvl,
                             'player_id': i.referral.id,
                             'referral_system_id': i.id,
                             'flag': i.referral_bonus})
        return Response(data, status=status.HTTP_200_OK)


class TakinReferralBonus(APIView):
    def post(self, request):
        person = get_object_or_404(Player, tg_id=request.data['tg_id'])
        system = get_object_or_404(ReferralSystem, id=request.data['referral_system_id'])
        if system.referral == person and system.referral_bonus == True:
            system.referral_bonus = False
            system.save()
            return Response({
                'name_box': 'Silver'})
        if system.new_person == person and system.new_person_bonus == True:
            system.new_person_bonus = False
            system.save()
            return Response({'name_box': 'Bronze'})
        else:
            return Response({'Error': "Вы уже получали бонус"}, status=status.HTTP_400_BAD_REQUEST)


class GenerateRefLinkView(APIView):
    def get(self, request, tg_id: int):
        try:
            create_link = f"https://t.me/FortuneMonster_bot?start=id_{tg_id}"
        except Exception as e:
            logging.error(f"Error generating referral link: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'ref_link': create_link}, status=status.HTTP_200_OK)
