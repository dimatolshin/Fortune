import{u as b,j as s,r as m,D as f}from"./index-BZhGot71.js";import{H as p}from"./Header-BraJ0-Vu.js";import{i as x}from"./imgCoin-DwLBqyid.js";import{u as y,q as j,x as h}from"./gueryClient-Cg1_ZnLl.js";import{u}from"./hooks-BDHb3lR9.js";import{i as w}from"./avatarFrend-L-lXDPIn.js";const N="_container_fkly5_2",k="_box_league_fkly5_12",v="_name_league_fkly5_27",C="_imgEnot_fkly5_38",z="_btn_left_fkly5_42",A="_btn_right_fkly5_60",E="_progress_fkly5_78",U="_progress_bar_fkly5_86",$="_title_energy_fkly5_97",q="_box_progress_fkly5_110",L="_iconCoin_fkly5_117",D="_box_all_users_fkly5_124",n={container:N,box_league:k,name_league:v,imgEnot:C,btn_left:z,btn_right:A,progress:E,progress_bar:U,title_energy:$,box_progress:q,iconCoin:L,box_all_users:D},H="/assets/woodenEnot-DUr-HAVk.png",S="_box_card_wszcs_1",B="_box_your_card_wszcs_9",F="_imgAvatar_wszcs_23",I="_user_info_wszcs_28",K="_name_user_wszcs_38",Q="_coin_window_wszcs_45",R="_coins_wszcs_50",T="_imgCoin_wszcs_59",V="_line_wszcs_67",r={box_card:S,box_your_card:B,imgAvatar:F,user_info:I,name_user:K,coin_window:Q,coins:R,imgCoin:T,line:V};function G({user:_}){const{tg_id:c}=b();return s.jsxs("div",{className:+c!==_.tg_id?r.box_card:r.box_your_card,children:[s.jsx("img",{src:w,className:r.imgAvatar}),s.jsxs("div",{className:r.user_info,children:[s.jsx("p",{className:r.name_user,children:_.name}),s.jsxs("div",{className:r.coin_window,children:[s.jsx("img",{src:x,className:r.imgCoin}),s.jsx("p",{className:r.coins,children:_.coin})]}),+c!==_.tg_id&&s.jsx("div",{className:r.line})]})]})}function Y(){const _=u(e=>{var o;return(o=e.dataUser.getUser)==null?void 0:o.coin}),c=u(e=>{var o;return(o=e.dataUser.getUser)==null?void 0:o.league}),[a,i]=m.useState(),[g,l]=m.useState(),{data:t}=y({queryKey:["dataLeagues"],queryFn:()=>h()},j);m.useEffect(()=>{if(t)switch(c){case"Деревянная":{const e=t.filter(o=>o.name==="Деревянная");i(e),l(e[0].players),console.log(e);break}case"Бронзовая":{const e=t.filter(o=>o.name==="Бронзовая");i(e),l(e[0].players);break}case"Серебрянная":{const e=t.filter(o=>o.name==="Серебрянная");i(e),l(e[0].players);break}}},[t]);const d=()=>{if(a&&_&&a[0].min_coin)return _*100/a[0].min_coin};return s.jsxs(f,{children:[s.jsx(p,{}),s.jsxs("div",{className:n.container,children:[s.jsxs("div",{className:n.box_league,children:[(a==null?void 0:a.length)&&s.jsx("h1",{className:n.name_league,children:a[0].name}),s.jsx("img",{className:n.imgEnot,src:H}),s.jsx("button",{className:n.btn_left}),s.jsx("button",{className:n.btn_right}),s.jsxs("div",{className:n.box_progress,children:[s.jsx("img",{src:x,className:n.iconCoin}),t&&a&&s.jsx("span",{className:n.title_energy,children:`${_} / ${a[0].min_coin}`})]}),s.jsx("div",{className:n.progress,children:s.jsx("div",{className:n.progress_bar,style:{width:`${d()}%`}})})]}),s.jsx("div",{className:n.box_all_users,children:g&&g.map(e=>s.jsx(G,{user:e}))})]})]})}export{Y as default};
