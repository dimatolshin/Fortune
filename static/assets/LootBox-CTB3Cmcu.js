import{j as s,u as F,r as t,m as $,n as Q,o as G}from"./index-Cv0sdWzb.js";import{D as K}from"./Dialog-NB8qpuXo.js";import{H as L}from"./Header-BH7Ck2O_.js";import{a as E,j as A,q as g,k as T,c as w,b as H,u as P,l as I}from"./gueryClient-CgYh_fR_.js";const M="_root_nngah_1",O="_container_nngah_14",U="_box_nngah_23",X="_imgBox1_nngah_35",Y="_imgEnotBack_nngah_46",Z="_slogan_nngah_57",J="_show_nngah_1",r={root:M,container:O,box:U,imgBox1:X,imgEnotBack:Y,slogan:Z,show:J},b="/assets/coinPrize-CayVTFUQ.png",z="/assets/energyPrize-CL1jtWuk.png",B="/assets/diamondsPrize-B0oiZMmn.png",k="/assets/botPrize-CLn2oDfX.png",R="/assets/skinPrize-Csi9GH01.png",v="/assets/box1-D3XQbKnU.png",C="/assets/box2-_a3OpZPI.png",D="/assets/box3-BQ05YlqY.png",V="/assets/EnotBackground-DEyn0Py-.png",W="_container_box_prize_1dudg_1",ss="_box_prize_1dudg_11",es="_imgEnotFace_1dudg_17",os="_loot_box_1dudg_28",is="_imgBox_1dudg_36",ns="_imgBumble_1dudg_43",ts="_box_info_prize_1dudg_51",cs="_possible_prize_1dudg_61",as="_title_prize_1dudg_75",rs="_box_getting_prize_1dudg_82",_s="_getting_prize_1dudg_88",ms="_imgPrize_1dudg_96",gs="_imgPrize1_1dudg_100",xs="_icon_prize_1dudg_104",o={container_box_prize:W,box_prize:ss,imgEnotFace:es,loot_box:os,imgBox:is,imgBumble:ns,box_info_prize:ts,possible_prize:cs,title_prize:as,box_getting_prize:rs,getting_prize:_s,imgPrize:ms,imgPrize1:gs,icon_prize:xs},ls="_btn_hu5ji_1",ps="_btn2_hu5ji_16",q={btn:ls,btn2:ps};function us({...n}){return s.jsx("button",{...n,className:q.btn,children:"Получить"})}const ds="/assets/EnotFaceBackground-CJx_fDe-.png",bs="/assets/bumbleLight-_3kQzhIG.png";function zs({...n}){return s.jsx("button",{...n,className:q.btn2,children:"Забрать"})}function y({box:n,lootBox1:i,imgBox:x}){const{tg_id:l}=F(),[c,a]=t.useState([]),[_,p]=t.useState(),{mutate:u}=E({mutationFn:e=>A(e.name_box),onSuccess:e=>{a(e),g.invalidateQueries({queryKey:["userData"]}),g.invalidateQueries({queryKey:["boxesData"]})}},g),j=E({mutationFn:e=>T(e.prizes,e.tg_id),onSuccess:e=>{p(e),g.invalidateQueries({queryKey:["userData"]})},onError:e=>{console.log(e)}},g),[d,h]=t.useState(1),N=()=>{(i==null?void 0:i.name)==="Bronze"&&u({name_box:"Bronze"}),(i==null?void 0:i.name)=="Silver"&&u({name_box:"Silver"}),(i==null?void 0:i.name)=="Gold"&&u({name_box:"Gold"}),h(2)},f=()=>{j.mutate({tg_id:l,prizes:c}),a([])};return t.useEffect(()=>{console.log(c)},[c]),s.jsxs("div",{className:o.container_box_prize,children:[s.jsx("img",{src:ds,className:o.imgEnotFace}),d==1&&s.jsxs("div",{className:o.box_prize,children:[s.jsxs("div",{className:o.loot_box,children:[s.jsx("img",{src:bs,className:o.imgBumble}),s.jsx("img",{className:o.imgBox,src:n})]}),s.jsxs("div",{className:o.box_info_prize,children:[s.jsx("p",{className:o.title_prize,children:"Ты можешь получить:"}),s.jsx("div",{className:o.possible_prize,children:x.map((e,m)=>s.jsx("img",{className:o.icon_prize,src:e},m))}),s.jsx(us,{onClick:N})]})]}),d==2&&s.jsxs("div",{className:o.box_getting_prize,children:[_?s.jsx("p",{className:o.title_prize,children:_.Success}):s.jsx("p",{className:o.title_prize,children:"Твоя награда!"}),s.jsx("div",{className:o.getting_prize,children:c.map((e,m)=>{if(e.prize_name==="Coin Boosts")return s.jsx("img",{className:o.imgPrize,src:b},m);if(e.prize_name==="Energy Boosts")return s.jsx("img",{className:o.imgPrize,src:z},m);if(e.prize_name==="Dimonds")return s.jsx("img",{className:o.imgPrize,src:B},m);if(e.prize_name==="Bot Boosts")return s.jsx("img",{className:o.imgPrize,src:k},m)})}),s.jsx(zs,{onClick:f,title:"Забрать"})]})]})}const Bs="_box_mth5q_1",js="_imgBox1_mth5q_13",S={box:Bs,imgBox1:js},hs=({onClick:n,imgBox:i})=>s.jsx("div",{onClick:n,className:S.box,children:s.jsx("img",{className:S.imgBox1,src:i})}),Ns=t.memo(hs);function Es(){const[n,i]=t.useState(0),x=w(),[l,c]=t.useState([]),{data:a}=H({queryKey:["boxesData"],queryFn:()=>I()},g);t.useEffect(()=>{a&&(x($(a[0])),x(Q(a[1])),x(G(a[2])))},[a]);const[_,p]=t.useState(""),u=P(e=>e.lootBox1.box),j=P(e=>e.lootBox2.box),d=P(e=>e.lootBox3.box),h=()=>{i(1),p(v),c([b,z,B])},N=()=>{i(2),p(C),c([b,z,B,k])},f=()=>{i(3),p(D),c([b,z,B,k,R])};return s.jsxs(K,{children:[s.jsx(L,{}),s.jsxs("div",{className:r.root,children:[n==0&&s.jsxs("div",{children:[s.jsx("h1",{className:r.slogan,children:"Текст призыв нажать на сундук"}),s.jsx("img",{src:V,className:r.imgEnotBack})]}),n==1&&s.jsx(y,{box:_,lootBox1:u,imgBox:l}),n==2&&s.jsx(y,{box:_,lootBox1:j,imgBox:l}),n==3&&s.jsx(y,{box:_,lootBox1:d,imgBox:l}),s.jsxs("div",{className:r.container,children:[s.jsx(Ns,{imgBox:v,onClick:h}),s.jsx("div",{onClick:N,className:r.box,children:s.jsx("img",{className:r.imgBox1,src:C})}),s.jsx("div",{onClick:f,className:r.box,children:s.jsx("img",{className:r.imgBox1,src:D})})]})]})]})}export{Es as default};
