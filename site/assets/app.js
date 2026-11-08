(function(){
"use strict";
// audience filter
var fb=[].slice.call(document.querySelectorAll("[data-who]"));
if(fb.length){
  var rows=[].slice.call(document.querySelectorAll(".row[data-levels]")),empty=document.getElementById("empty"),cnt=document.getElementById("count");
  var apply=function(v){var n=0;rows.forEach(function(r){var ok=v==="all"||r.dataset.levels.split(" ").indexOf(v)>-1;r.hidden=!ok;if(ok)n++});
    fb.forEach(function(b){b.setAttribute("aria-pressed",b.dataset.who===v)});if(empty)empty.hidden=n>0;if(cnt)cnt.textContent=n;
    try{history.replaceState(null,"",v==="all"?location.pathname:"#"+v)}catch(e){}};
  fb.forEach(function(b){b.addEventListener("click",function(){apply(b.dataset.who)})});
  var h=location.hash.slice(1);apply(fb.some(function(b){return b.dataset.who===h})?h:"all");
}
// decks
[].forEach.call(document.querySelectorAll(".deck"),function(d){
  var s=[].slice.call(d.querySelectorAll(".slide")),i=0,c=d.querySelector(".cnt"),b=d.querySelector(".bar i");
  function show(n){i=Math.max(0,Math.min(s.length-1,n));s.forEach(function(x,k){x.classList.toggle("on",k===i)});c.textContent=(i+1)+" / "+s.length;b.style.width=((i+1)/s.length*100)+"%";
    var nx=s[i+1]&&s[i+1].querySelector("img");if(nx&&!nx.complete)nx.loading="eager"}
  d.querySelector("[data-prev]").onclick=function(){show(i-1)};
  d.querySelector("[data-next]").onclick=function(){show(i+1)};
  d.querySelector("[data-full]").onclick=function(){if(document.fullscreenElement)document.exitFullscreen();else if(d.requestFullscreen)d.requestFullscreen()};
  d.tabIndex=0;
  d.addEventListener("keydown",function(e){if(e.key==="ArrowRight"||e.key===" "||e.key==="PageDown"){e.preventDefault();show(i+1)}else if(e.key==="ArrowLeft"||e.key==="PageUp"){e.preventDefault();show(i-1)}else if(e.key==="Home")show(0);else if(e.key==="End")show(s.length-1)});
  var x0=null;d.addEventListener("touchstart",function(e){x0=e.touches[0].clientX},{passive:true});
  d.addEventListener("touchend",function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)show(i+(dx<0?1:-1));x0=null});
  show(0);
});
// tabs
[].forEach.call(document.querySelectorAll("[data-tabs]"),function(t){
  var bs=[].slice.call(t.querySelectorAll("button")),ps=[].slice.call(document.querySelectorAll("[data-panel]"));
  bs.forEach(function(b){b.addEventListener("click",function(){bs.forEach(function(x){x.setAttribute("aria-selected",x===b)});ps.forEach(function(p){p.hidden=p.dataset.panel!==b.dataset.tab})})});
});
var pr=document.getElementById("print");if(pr)pr.onclick=function(){window.print()};
})();
