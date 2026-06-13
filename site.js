/* HFFA Local 1463 — shared site behaviors.
   Loaded on every page with `defer`. Page-specific blocks (post filter,
   counters, forms) no-op when their elements are absent. */
(function(){
  "use strict";
  var root=document.documentElement, STORE="hffa-a11y", live=document.getElementById("liveRegion");
  function announce(m){ if(live){ live.textContent=""; setTimeout(function(){ live.textContent=m; },60); } }

  /* ---- Accessibility prefs ---- */
  var prefs={size:100,hc:false,readable:false,motion:false,underline:false};
  try{ Object.assign(prefs, JSON.parse(localStorage.getItem(STORE)||"{}")); }catch(e){}
  function applyPrefs(){
    root.style.fontSize=prefs.size+"%";
    root.classList.toggle("hc",!!prefs.hc);
    root.classList.toggle("readable",!!prefs.readable);
    root.classList.toggle("reduce",!!prefs.motion);
    root.classList.toggle("underline",!!prefs.underline);
    var hc=document.getElementById("tHc"); if(hc) hc.checked=!!prefs.hc;
    var rd=document.getElementById("tReadable"); if(rd) rd.checked=!!prefs.readable;
    var mo=document.getElementById("tMotion"); if(mo) mo.checked=!!prefs.motion;
    var ul=document.getElementById("tUnderline"); if(ul) ul.checked=!!prefs.underline;
    var arr=document.querySelectorAll(".textsize");
    for(var i=0;i<arr.length;i++){ arr[i].setAttribute("aria-pressed", String(prefs.size)===arr[i].dataset.size?"true":"false"); }
  }
  function save(){ try{ localStorage.setItem(STORE,JSON.stringify(prefs)); }catch(e){} }
  applyPrefs();
  (function(){ var arr=document.querySelectorAll(".textsize");
    for(var i=0;i<arr.length;i++){ (function(b){ b.addEventListener("click",function(){ prefs.size=parseInt(b.dataset.size,10); applyPrefs(); save(); announce("Text size "+prefs.size+" percent"); }); })(arr[i]); }
  })();
  function bindToggle(id,key,label){ var el=document.getElementById(id); if(!el) return; el.addEventListener("change",function(e){ prefs[key]=e.target.checked; applyPrefs(); save(); announce(label+(e.target.checked?" on":" off")); }); }
  bindToggle("tHc","hc","High contrast");
  bindToggle("tReadable","readable","Readable font");
  bindToggle("tMotion","motion","Reduce motion");
  bindToggle("tUnderline","underline","Underline links");
  var resetBtn=document.getElementById("a11yReset");
  if(resetBtn) resetBtn.addEventListener("click",function(){ prefs={size:100,hc:false,readable:false,motion:false,underline:false}; applyPrefs(); save(); announce("Accessibility settings reset"); });

  /* ---- Panel open/close + focus trap ---- */
  var panel=document.getElementById("a11yPanel"), overlay=document.getElementById("a11yOverlay"), lastFocus=null;
  function focusable(c){ return Array.prototype.slice.call(c.querySelectorAll("button,[href],input,select,[tabindex]:not([tabindex='-1'])")).filter(function(el){ return !el.disabled && el.offsetParent!==null; }); }
  function openPanel(){ if(!panel) return; lastFocus=document.activeElement; panel.hidden=false; requestAnimationFrame(function(){ panel.classList.add("open"); overlay.classList.add("open"); }); document.body.style.overflow="hidden"; document.getElementById("a11yClose").focus(); }
  function closePanel(){ if(!panel) return; panel.classList.remove("open"); overlay.classList.remove("open"); document.body.style.overflow=""; setTimeout(function(){ panel.hidden=true; },220); if(lastFocus&&lastFocus.focus) lastFocus.focus(); }
  ["a11yFab","a11yOpen"].forEach(function(id){ var el=document.getElementById(id); if(el) el.addEventListener("click",function(){ closeMobile(); openPanel(); }); });
  var closeBtn=document.getElementById("a11yClose"); if(closeBtn) closeBtn.addEventListener("click",closePanel);
  var doneBtn=document.getElementById("a11yDone"); if(doneBtn) doneBtn.addEventListener("click",closePanel);
  if(overlay) overlay.addEventListener("click",closePanel);
  if(panel) panel.addEventListener("keydown",function(e){
    if(e.key==="Escape"){ closePanel(); return; }
    if(e.key==="Tab"){ var f=focusable(panel); if(!f.length) return; var first=f[0], last=f[f.length-1];
      if(e.shiftKey&&document.activeElement===first){ e.preventDefault(); last.focus(); }
      else if(!e.shiftKey&&document.activeElement===last){ e.preventDefault(); first.focus(); } }
  });

  /* ---- Mobile nav ---- */
  var mNav=document.getElementById("mobileNav"), mOv=document.getElementById("mobileOverlay"), navToggle=document.getElementById("navToggle");
  function openMobile(){ if(!mNav) return; mNav.hidden=false; mOv.hidden=false; requestAnimationFrame(function(){ mNav.classList.add("open"); mOv.classList.add("open"); }); navToggle.setAttribute("aria-expanded","true"); document.getElementById("navClose").focus(); }
  function closeMobile(){ if(!mNav || mNav.hidden) return; mNav.classList.remove("open"); mOv.classList.remove("open"); navToggle.setAttribute("aria-expanded","false"); setTimeout(function(){ mNav.hidden=true; mOv.hidden=true; },220); }
  if(navToggle) navToggle.addEventListener("click",openMobile);
  var navClose=document.getElementById("navClose"); if(navClose) navClose.addEventListener("click",function(){ closeMobile(); navToggle.focus(); });
  if(mOv) mOv.addEventListener("click",closeMobile);
  if(mNav){ mNav.addEventListener("keydown",function(e){ if(e.key==="Escape"){ closeMobile(); navToggle.focus(); } });
    var mlinks=mNav.querySelectorAll("a"); for(var i=0;i<mlinks.length;i++){ mlinks[i].addEventListener("click",closeMobile); } }

  /* ---- Post filtering (home only) ---- */
  var grid=document.getElementById("postGrid");
  if(grid){
    var fbtns=document.querySelectorAll(".filter-btn"), cards=grid.querySelectorAll(".post-card"), fstatus=document.getElementById("filterStatus");
    var applyFilter=function(val){
      var shown=0;
      for(var i=0;i<cards.length;i++){ var match=(val==="all"||cards[i].dataset.tag===val); cards[i].style.display=match?"":"none"; if(match) shown++; }
      for(var j=0;j<fbtns.length;j++){ fbtns[j].setAttribute("aria-pressed", fbtns[j].dataset.filter===val?"true":"false"); }
      if(fstatus) fstatus.textContent=(val==="all"?"Showing all posts":"Showing "+shown+" "+val+" post"+(shown===1?"":"s"));
    };
    for(var k=0;k<fbtns.length;k++){ (function(b){ b.addEventListener("click",function(){ applyFilter(b.dataset.filter); }); })(fbtns[k]); }
  }

  /* ---- Stat counters ---- */
  var reduceMotion=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function runCount(el){
    var target=parseInt(el.dataset.target,10), suffix=el.dataset.suffix||"";
    if(prefs.motion||reduceMotion){ el.textContent=target.toLocaleString()+suffix; return; }
    var start=null, dur=1300;
    function step(ts){ if(!start)start=ts; var p=Math.min((ts-start)/dur,1), e=1-Math.pow(1-p,3); el.textContent=Math.floor(e*target).toLocaleString()+suffix; if(p<1)requestAnimationFrame(step); else el.textContent=target.toLocaleString()+suffix; }
    requestAnimationFrame(step);
  }
  var counters=document.querySelectorAll(".count");
  if(counters.length){
    if("IntersectionObserver" in window){
      var io=new IntersectionObserver(function(entries){ entries.forEach(function(en){ if(en.isIntersecting){ runCount(en.target); io.unobserve(en.target); } }); },{threshold:.4});
      for(var c=0;c<counters.length;c++){ io.observe(counters[c]); }
    } else { for(var d=0;d<counters.length;d++){ runCount(counters[d]); } }
  }

  var yr=document.getElementById("yr"); if(yr) yr.textContent=new Date().getFullYear();
})();

/* ---- Forms: validate + submit to Netlify Forms via AJAX ---- */
(function(){
  function encode(data){ return Object.keys(data).map(function(k){ return encodeURIComponent(k)+"="+encodeURIComponent(data[k]); }).join("&"); }
  var forms = document.querySelectorAll("form[data-netlify='true']");
  for (var i=0;i<forms.length;i++){ (function(form){
    var status = form.querySelector(".form-status");
    function setField(field, invalid){ field.setAttribute("data-invalid", invalid ? "true" : "false"); var inp=field.querySelector("input,select,textarea"); if(inp) inp.setAttribute("aria-invalid", invalid?"true":"false"); }
    function validate(){
      var ok=true, firstBad=null;
      var reqs = form.querySelectorAll(".field [required]");
      for (var j=0;j<reqs.length;j++){
        var inp=reqs[j], field=inp.closest(".field"), bad=false;
        if (!inp.value.trim()) bad=true;
        else if (inp.type==="email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value.trim())) bad=true;
        setField(field, bad); if(bad){ ok=false; if(!firstBad) firstBad=inp; }
      }
      if(firstBad) firstBad.focus();
      return ok;
    }
    form.addEventListener("submit", function(e){
      e.preventDefault();
      if(status){ status.className="form-status"; status.textContent=""; }
      if(!validate()){ if(status){ status.className="form-status err"; status.textContent="Please fix the highlighted fields."; } return; }
      var data={}; new FormData(form).forEach(function(v,k){ data[k]=v; });
      fetch("/", { method:"POST", headers:{"Content-Type":"application/x-www-form-urlencoded"}, body:encode(data) })
        .then(function(r){ if(!r.ok) throw new Error(); if(status){ status.className="form-status ok"; status.textContent="Mahalo! Your message was received. The HFFA office will be in touch."; } form.reset(); })
        .catch(function(){ if(status){ status.className="form-status err"; status.textContent="Sorry — something went wrong. Please call the office at 808-949-1566."; } });
    });
  })(forms[i]); }
})();
