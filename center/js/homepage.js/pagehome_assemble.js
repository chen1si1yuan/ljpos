!(function(){
  var box_div = document.createElement('div');
  var str = '<div class="navbar">\
  <div class="left_nav_box">\
      <ul class="left_nav_list">\
          <li>首页</li>\
          <li>应用</li>\
          <li>服务列表</li>\
          <li>解决方案</li>\
          <li>帮助中心</li>\
      </ul>\
  </div>\
  <div class="right_nav_box">\
      <ul class="right_nav_list">\
          <li>登录</li>\
          <li>注册</li>\
      </ul>\
  </div>\
</div>';
    box_div.innerHTML = str;
    document.body.appendChild(box_div);
    var stylestr = " *{\
        list-style: none;\
        padding: 0;\
        margin: 0;\
    }\
    .navbar{\
        position: absolute;\
        left: 0;\
        right: 0;\
        top: 0;\
        height: 120px;\
        background-color: #ccc;\
        line-height: 120px;\
        font-size: 0;\
        color: #000;\
        min-width:100%;\
        z-index:-999;\
    }\
    .left_nav_box{\
        height: 120px;;\
        width: 50%;\
        display: inline-block;\
        text-align: center;\
    }\
    .left_nav_box li{\
        display: inline-block;\
        font-size: 23px;\
        margin-left: 30px;\
        cursor: pointer;\
    }\
    .right_nav_box{\
        height: 120px;;\
        width: 50%;\
        display: inline-block;\
        text-align: right;\
    }\
    .right_nav_box li{\
       display: inline-block;\
        font-size: 20px;\
        margin-right: 30px;\
        cursor: pointer;\
    }";
    var styl = document.createElement('style');
    styl.innerHTML = stylestr;
    document.head.appendChild(styl);

})()