import{j as s,r as e,D as x}from"./index-DRmcogro.js";import{i as l}from"./imgCoin-DwLBqyid.js";import{M as m}from"./Modal-CSllgJHv.js";import{H as d}from"./Header-DzDMrUmA.js";const j="_container_zbioi_1",b="_iconX_zbioi_14",f="_box_info_task_zbioi_25",h="_name_task_zbioi_31",g="_box_cost_zbioi_39",k="_icon_coin_zbioi_44",N="_arrow_zbioi_52",C="_cost_task_zbioi_57",n={container:j,iconX:b,box_info_task:f,name_task:h,box_cost:g,icon_coin:k,arrow:N,cost_task:C};function p(){return s.jsx("svg",{width:"9",height:"16",viewBox:"0 0 9 16",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:s.jsx("path",{d:"M1.00456 14.0813C0.684352 14.4049 0.683236 14.9306 1.00207 15.2555C1.29191 15.551 1.7464 15.5787 2.06721 15.3383L2.15915 15.2581L8.75915 8.58894C9.05112 8.29392 9.07768 7.83103 8.83882 7.50546L8.7592 7.41221L2.1592 0.741981C1.83902 0.418393 1.32097 0.419481 1.00212 0.744412C0.712245 1.0398 0.686779 1.50114 0.925101 1.8257L1.00451 1.91866L7.022 8.00089L1.00456 14.0813Z",fill:"#BEBEBE"})})}const u="_modal_content_1ec73_1",v="_iconX_1ec73_10",X="_title_1ec73_15",E="_box_title_1ec73_26",w="_btn_1ec73_36",L="_coin_box_1ec73_55",z="_iconCoin_1ec73_65",$="_coin_title_1ec73_72",B="_imgEnot_1ec73_82",o={modal_content:u,iconX:v,title:X,box_title:E,btn:w,coin_box:L,iconCoin:z,coin_title:$,imgEnot:B},M="/assets/iconX-CgXIbL1C.png",y="/assets/imgEnot-BGlfNUJC.png";function T({onClose:c}){return s.jsx(s.Fragment,{children:s.jsxs("div",{className:o.modal_content,children:[s.jsxs("div",{className:o.box_title,children:[s.jsx("img",{src:M,className:o.iconX}),s.jsx("p",{className:o.title,children:"Следи за нашим аккаунтом в X"})]}),s.jsx("button",{onClick:c,className:o.btn,children:"Подписаться"}),s.jsxs("div",{className:o.coin_box,children:[s.jsx("img",{src:l,className:o.iconCoin}),s.jsx("p",{className:o.coin_title,children:"+5 000"})]}),s.jsx("img",{src:y,className:o.imgEnot})]})})}function t(){const[c,_]=e.useState(!1),r=()=>{_(!0)},a=()=>{_(!1)};return e.useEffect(()=>{},[c]),s.jsxs("div",{onClick:r,className:n.container,children:[s.jsx("div",{className:n.iconX}),s.jsxs("div",{className:n.box_info_task,children:[s.jsx("p",{className:n.name_task,children:"Следи за нашим аккаунтом в X"}),s.jsxs("div",{className:n.box_cost,children:[s.jsx("img",{className:n.icon_coin,src:l}),s.jsx("p",{className:n.cost_task,children:"+ 5000"})]})]}),s.jsx("div",{className:n.arrow,children:s.jsx(p,{})}),s.jsx(m,{isOpen:c,onClose:a,hiddenClose:!0,children:s.jsx(T,{onClose:a})})]})}const D="_container_f94sl_1",H="_box_fon_f94sl_10",I="_slogan1_f94sl_20",S="_slogan2_f94sl_39",V="_title_list_tasks_f94sl_56",A="_box_all_tasks_f94sl_69",i={container:D,box_fon:H,slogan1:I,slogan2:S,title_list_tasks:V,box_all_tasks:A};function R(){return s.jsxs(x,{children:[s.jsx(d,{}),s.jsxs("div",{className:i.container,children:[s.jsxs("div",{className:i.box_fon,children:[s.jsx("p",{className:i.slogan1,children:"ЗАРАБОТАЙ"}),s.jsx("p",{className:i.slogan2,children:"БОЛЬШЕ МОНЕТ"}),s.jsx("p",{className:i.title_list_tasks,children:"Список заданий"})]}),s.jsxs("div",{className:i.box_all_tasks,children:[s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{}),s.jsx(t,{})]})]})]})}export{R as default};
