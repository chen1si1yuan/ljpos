<template>
    <div id="header">
        <!-- 头部菜单栏 -->
        <header>
            <div class="header-logo">
                <router-link to="/Mainpage" >
                    <img @click="navListChange('index')" :src="pagedata.imgResources.headerLogoUrl" alt="首页/logo图片">
                </router-link>
            </div>
            <nav class="header-navlist">
                <ul class="header-nav">                    
                    <li :class="{'menu-actived' :item.keyword === getCurrentNavList}"  
                    v-for="(item, index) in pagedata.headerNavList" :key="index" 
                    @click="navListChange(item.keyword)" ><router-link :to="item.link">{{item.value}}</router-link></li>                   
                </ul>
            </nav>
            <div class="login-register">
                <div class="isLogin-false" v-if="!getUserIsLogin">
                    <div class="login" @click="isOpenDialogChange('login')" >登录</div>
                    <div class="register" @click="isOpenDialogChange('register')">注册</div>
                </div>
                <div class="isLogin-true nav-info" v-if="getUserIsLogin">
                    <div class="username">欢迎您，<span>{{userInfo.userNickName}}</span></div>
                   <!--  <div class="userlogo"><img :src="userInfo.userLogoUrl" alt="用户头像"></div>   -->                  
                </div>
                <ul class="isLogin-true menu-info" v-if="getUserIsLogin">
                    <li class="username-isidentificate">
                        <p>{{userInfo.userNickName}}</p>
                        <p>{{userInfo.isidentificate_msg}}</p>
                    </li>
                    <li class="usermenu" v-for="(item, index) in userInfo.userMenu" :key="index">
                        <!-- <img :src="item.ilogo" alt=""> -->
                        <span :class="item.ilogo"></span> 
                        <router-link :to='item.link' @click.native="setCurrentSecondNav(item.go)">{{item.name}}</router-link>                     
                    </li>                    
                </ul>             
            </div>
        </header>
        
        <div class="dialog-container" v-if="pagestatus.isOpenDialog" >
            <!-- 登录注册对话框 -->
            <div class="dialog-inner-container dialog-login-register" v-if ="pagestatus.dialogType === 'login-register' ">
                <div class="dialog-box">
                    <!-- 对话导航栏 -->
                    <div class="dialog-title">
                        <nav :class="{'nav-actived':pagestatus.loginToRegister === 'login' }" 
                        @click.stop.prevent="loginToRegisterChange('login')" >登录</nav>
                        <nav :class="{'nav-actived':pagestatus.loginToRegister === 'register' }" 
                        @click.stop.prevent="loginToRegisterChange('register')">注册</nav>
                    </div>
                    <!-- 对话框取消 -->
                    <div class="dialog-close" @click.stop.prevent="isOpenDialogChange()">&nbsp;x&nbsp;</div>
                    <!-- 对话内容 -->
                    <div class="dialog-content">
                        <!-- 登录 -->
                        <div class="login-content" v-if="pagestatus.loginToRegister === 'login' ">
                            <form action="" method="post">
                                <input type="text" name="loginusertel" id="loginusertel" placeholder="手机号"
                                v-model.number="formData.login.userTelNumber" @blur='dataCheck("logintel")' >
                                <input type="password" name="loginuserpwd" id="loginuserpwd"  placeholder="密码（不少于8位）"
                                v-model="formData.login.userPassword" @blur='dataCheck("loginpwd")' >
                                <div class="input-item login-vercode">
                                    <input type="text" name="loginvercode" id="loginvercode" placeholder="验证码"
                                    v-model="formData.login.verCode" @blur='dataCheck("logincode")' >
                                    <div class="vercode-img" @click.stop.prevent="loginVerCodeChange()" >
                                        <img :src="pagedata.imgResources.loginVerCodeUrl" ref="refVerCodeImg" alt="验证码" title="看不清，单击换一张">
                                    </div>
                                    <input type="button" @click.stop.prevent="loginVerCodeChange()" value="换一张">
                                </div>
                                <div class="input-item login-otherinfo">
                                    <div class="checkbox">
                                        <input type="checkbox" name="autologin" id="autologin" v-model="formData.login.isAutoLogin">
                                        <i @click="isAutoLoginChange()"></i>
                                        <label for="autologin">下次自动登录</label>
                                    </div>
                                    <input type="button" @click.stop.prevent="dialogTypeChange('changePassword')" class="forgetpwd" value="忘记密码 ？快点这里">
                                </div>
                                <input type="submit" @click.stop.prevent="submitLogin()" value="登录">
                                <!-- 状态消息 -->
                                <div class="message login-status" v-if="pagestatus.messageinfo.ishow">{{pagestatus.messageinfo.value}}</div>
                            </form>
                        </div>
                        <!-- 注册 -->
                        <div class="register-content" v-if="pagestatus.loginToRegister === 'register' ">
                            <form action="" method="post">
                                <input type="text" name="regusertel" id="regusertel" placeholder="手机号"
                                v-model="formData.register.userTelNumber" @blur='dataCheck("registertel")' >
                                <div class="input-item vercode vercode-tel">
                                    <input type="text" name="regtelcode" id="regtelcode" placeholder="短信验证码"
                                   v-model="formData.register.telVerCode" @blur='dataCheck("registertelcode")' >
                                    <input type="button" @click.stop.prevent="getRegTelCode()" value="获取验证码">
                                </div>
                                <input type="password" name="reguserpwd" id="reguserpwd" placeholder="密码（不少于8位）"
                                v-model="formData.register.userPassword" @blur='dataCheck("registerpwd")' >
                                <input type="password" name="regokuserpwd" id="regokuserpwd" placeholder="确认密码" 
                                v-model="formData.register.okUserPassword" @blur='dataCheck("registerokpwd")' >
                                <div class="input-item reg-text"><p>点击注册按钮代表您已阅读并同意</p><a href="" @click.stop.prevent="userTreaty()">《用户使用条约》</a></div>
                                <input type="submit" @click.stop.prevent="submitRegister()" value="注册">
                                <!-- 状态消息 -->
                                <div class="message reg-status" v-if="pagestatus.messageinfo.ishow">{{pagestatus.messageinfo.value}}</div>
                            </form>            
                        </div>                        
                    </div>
                </div>
            </div>

            <!-- 忘记密码注册框 -->
            <div class="dialog-inner-container dialog-forget-password" v-if="pagestatus.dialogType === 'changePassword' ">
                <div class="dialog-box">
                    <!-- 对话框标题 -->
                    <div class="dialog-title">
                        <nav class="nav-actived">忘记密码</nav>
                    </div>
                    <!-- 对话框取消 -->
                    <div class="dialog-close" @click.stop.prevent="isOpenDialogChange()">&nbsp;x&nbsp;</div>
                    <!-- 对话框内容 -->
                    <div class="dialog-content">
                        <div class="forgetpwd-content">
                            <form action="" method="post">
                                <input type="text" name="regusertel" id="regusertel" placeholder="手机号"
                                v-model="formData.forgetPwd.userTelNumber" @blur='dataCheck("changepwdtel")' >
                                <div class="input-item vercode vercode-tel">
                                    <input type="text" name="regtelcode" id="regtelcode" placeholder="短信验证码"
                                    v-model="formData.forgetPwd.telVerCode" @blur='dataCheck("changepwdtelcode")' >
                                    <input type="button" @click.stop.prevent="getRegTelCode()" value="获取验证码">
                                </div>
                                <input type="password" name="reguserpwd" id="reguserpwd" placeholder="新密码（不少于8位）"
                                v-model="formData.forgetPwd.userPassword" @blur='dataCheck("changepwdpwd")' >
                                <input type="password" name="regokuserpwd" id="regokuserpwd" placeholder="确认新密码" 
                                v-model="formData.forgetPwd.okUserPassword" @blur='dataCheck("changepwdokpwd")' >                                
                                <input type="submit" @click.stop.prevent="submitChangePwd()" value="更改密码">
                                <!-- 状态消息 -->
                                <div class="message forgetpwd-status" v-if="pagestatus.messageinfo.ishow">{{pagestatus.messageinfo.value}}</div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import headerLogoUrl from '@/assets/img/header/logo@2x.png';


export default {
  data() {
    return {
        /* 页面公共数据 */
        pagedata: {
            /* 菜单导航栏 */
            headerNavList: [
                {keyword: 'servive', value: '服务商城', link: '/Servive'},
                {keyword: 'solutions', value: '解决方案', link: '/Solutions',subNav: []},
                {keyword: 'application', value: '创建应用', link: '/Application',subNav: []},
                {keyword: 'help', value: '帮助中心', link: '/Help'},
            ],
            /* 图片资源 /login/verificationCode*/
            imgResources: {
                headerLogoUrl,                
                loginVerCodeUrl: 'http://192.168.1.161:8080/login/verificationCode'
            }           
        },
        /* 用户信息 */
        userInfo: {
            userLogoUrl: '',
            userNickName: this.$store.state.publicData.userinfo.userNickName,
            isidentificate_msg: this.$store.state.publicData.userinfo.isIdentificate_msg,
            userMenu: [
                {
                    ilogo: 'fa fa-user',
                    name: '个人信息',               
                    link: '/Personcenter/Presoninfo', 
                    go:'PresonInfo-baseinfo'                   
                },
                {
                    ilogo: 'fa fa-th-large',
                    name: '我的应用',                    
                    link: '/Personcenter/Myapp',
                    go:'MyApp-list'
                },
                {
                    ilogo: 'fa fa-question-circle-o',
                    name: '问题反馈',                    
                    link: '/Personcenter/Problem',
                    go:'Problem-create'
                },
                {
                    ilogo: 'fa fa-sign-out',
                    name: '退出登录',                    
                    link: '',
                    go: 'exit'
                }

            ]
            
        },
        /* 页面状态数据 */
        pagestatus: {            
            dialogType: 'login-register',
            isOpenDialog: false,            
            loginToRegister: null,
            messageinfo: {ishow: false ,value: '出错，请刷新网页重新操作'}
        },
        /* 表单数据绑定 */
        formData: {
            login: {
                userTelNumber: '',
                userPassword: '',
                verCode: '',
                isAutoLogin: false
            },
            register: {
                userTelNumber: '',
                telVerCode: '',
                userPassword: '',
                okUserPassword: ''
            },
            forgetPwd: {
                userTelNumber: '',
                telVerCode: '',
                userPassword: '',
                okUserPassword: ''
            }
        }        
    }
  },
  mounted:function() {
      /* this.userNickName = this.$store.state.publicData.userNickName;
      this.isidentificate_msg = this.$store.state.publicData.isIdentificate_msg; */
  },
  computed: {
      getUserIsLogin() {
          return this.$store.state.pageStatus.user.isLogin;
      },
      getCurrentNavList() {
          return this.$store.state.pageStatus.header.currentNavList;
      }
      /* ,
      getUserBaseinfo() {
          return {
              count: this.$store.state.publicData.userCount,
              userNickName: this.$store.state.publicData.userNickName,
              isidentificate: this.$store.state.publicData.isIdentificate,
          }
      }   */     
    },
  methods: {
        /* 当前活动菜单导航栏 */
        navListChange(key) {
            this.$store.state.pageStatus.header.currentNavList = key;
        }, 
        /* 对话框类型变换 */
        dialogTypeChange(type) {
            this.pagestatus.messageinfo.ishow = false;
            /* type类型：登录注册login-register 忘记密码changePassword */
            switch (type) {
                case 'login-register':
                    this.pagestatus.dialogType = type;
                    break;
                case 'changePassword':
                    this.pagestatus.dialogType = type;
                    break;
                default:
                    break;
            }
        },
        /* 开启登录或者注册对话框 */     
        isOpenDialogChange(val) {
            if(val) {
                this.pagestatus.messageinfo.ishow = false;
                this.pagestatus.isOpenDialog = true;
                this.pagestatus.loginToRegister = val;            
            }else{
                this.pagestatus.messageinfo.ishow = false;              
                this.pagestatus.isOpenDialog = false;                
                this.pagestatus.loginToRegister = null;
                this.pagestatus.dialogType = 'login-register';                
            }
        },
        /* 自动登录状态切换 */
        isAutoLoginChange() {
            this.formData.login.isAutoLogin = !this.formData.login.isAutoLogin;
        },
        /* 登录注册状态切换 */
        loginToRegisterChange(val) {
            this.pagestatus.messageinfo.ishow = false;
            this.pagestatus.loginToRegister = val;
        },
        /* 图片验证码 */
        loginVerCodeChange() {
            let imgTime=new Date().getTime();
            this.$refs.refVerCodeImg.src = 'http://192.168.1.161:8080/login/verificationCode?'+imgTime;       
        },
        /* 获取手机验证码 */
        getRegTelCode() {
            let params = new URLSearchParams();           
            let account = this.formData.forgetPwd.userTelNumber;
            params.append('account', account);            
            if(this.userTelNumCheck(account).status){
                this.$axios({
                    method: "post",
                    url: '/regist/getPhoneVCode',
                    data: params
                })
                .then(function(res) {
                    console.log('验证码已发送至'+account+'手机');
                    console.log(res);
                })
                .catch(function(err) {
                    console.log(err);
                });
            }else{
                console.log('手机号不争气');
            }   
        },        
        /* 登录按钮 */
        submitLogin() {
            let that = this;                      
            let params = new URLSearchParams();
            let account = that.formData.login.userTelNumber;
            let password = that.formData.login.userPassword;
            let verificationCode = that.formData.login.verCode;
            let autoLogin = that.formData.login.isAutoLogin;
            params.append('account', account);
            params.append('password', password);
            params.append('verificationCode', verificationCode);
            params.append('autoLogin', autoLogin);
            if(params){
                this.$axios({
                method: "post",
                url: '/login/doLogin',
                data: params
            })            
            .then(function(res) {
                let result = res.data;
                if(result.state == 200) {
                    this.$store.state.pageStatus.user.isLogin = true;

                    let obj = {
                        status: false,
                        message: result.msg
                    }
                    that.setDialogMessage(obj);
                }else{
                    let obj = {
                        status: false,
                        message:result.msg
                    }
                    that.setDialogMessage(obj);
                }
            })
            .catch(function(err) {
                console.log(err);
            });
            }

        },
        /* 注册按钮 */
        submitRegister() {
            let that = this;
            let params = new URLSearchParams();
            let account = that.formData.register.userTelNumber;
            let password = that.formData.register.userPassword;
            let verificationCode = that.formData.register.telVerCode;
            params.append('account', account);
            params.append('password', password);
            params.append('verificationCode', verificationCode);
            if(params){
                this.$axios({
                method: "post",
                url: '/regist/doRegist',
                data: params
            })
            .then(function(res) {
                let result = res.data;
                if(result.state == 200) {
                    let obj = {
                        status: false,
                        message: result.msg
                    }
                    that.setDialogMessage(obj);
                }else{
                    let obj = {
                        status: false,
                        message:result.msg
                    }
                    that.setDialogMessage(obj);
                }
            })
            .catch(function(err) {
                console.log(err);
            });
            }
        },
        /* 找回密码 */
        submitChangePwd() {
            let that = this;
            let params = new URLSearchParams();
            let account = that.formData.forgetPwd.userTelNumber;
            let password = that.formData.forgetPwd.userPassword;
            let verificationCode = that.formData.forgetPwd.telVerCode;
            params.append('account', account);
            params.append('password', password);
            params.append('verificationCode', verificationCode);
            if(params){
                this.$axios({
                method: "post",
                url: '/regist/findBackPWD',
                data: params
            })
            .then(function(res) {
                let result = res.data;
                if(result.state == 200) {
                    let obj = {
                        status: false,
                        message: result.msg
                    }
                    that.setDialogMessage(obj);
                }else{
                    let obj = {
                        status: false,
                        message:result.msg
                    }
                    that.setDialogMessage(obj);
                }
            })
            .catch(function(err) {
                console.log(err);
            });
            }
        },
        /* 阅读用户条约 */
        userTreaty() {
            alert('阅读用户条约');
        },
        /* 手机号正则 */      
        userTelNumCheck(num) {
            /* 手机号规则：11位纯数字并以1开头，以3，4，5，7，8作为第二位 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入您的手机号"
                }
            }
            let regex = /^1[34578]\d{9}$/;
            if(!regex.test(num)){
                return {
                    status: false,
                    message: '请正确输入11位手机号'
                }
            }else{
                return {
                    status: true,
                    message: '手机号验证成功'
                }
            }
        },
        /* 密码正则 */
        userPwdNumCheck(num) {
            /* 规则：8-20位数字和大小写字母的混合体 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入您的密码"
                }
            }            
            let regex = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,12}$/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请输入8-20位数字和字母的混合体'
                }
            }else{
                return {
                    status: true,
                    message: '密码验证成功'
                }
            }       
        },
        /* 手机验证码正则 */
        telVerCodeCheck(num) {
            /* 规则：4位纯数字 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入手机验证码"
                }
            }           
            let regex = /^\d{4}$/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请输入正确的手机验证码'
                }
            }else{
                return {
                    status: true,
                    message: '手机验证码验证成功'
                }
            }       
        },
        /* 图片验证码正则 */
        verCodeCheck(num) {
            /* 规则：4位数字和大小写字母的混合体 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入验证码"
                }
            }            
            let regex = /^[0-9A-Za-z]{4}$/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请输入正确的验证码'
                }
            }else{
                return {
                    status: true,
                    message: '验证码验证成功'
                }
            }     
        },
        /* 数据检查dataCheck */
        dataCheck(type) {
            /* type类： 登录手机号logintel 登录密码loginpwd 登录验证码logincode
                        注册手机号registertel 手机验证码registertelcode 注册密码registerpwd 确认密码registerokpwd
                        忘记密码->手机号changepwdtel 手机验证码changepwdtelcode 新密码changepwdpwd 确认新密码changepwdokpwd
            */
            value = value.trim();
            let checkData = null,result = null;
            switch (type) {
                /* 登录 */
                case 'logintel':
                    checkData = this.formData.login.userTelNumber;
                    result = this.userTelNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'loginpwd':
                    checkData = this.formData.login.userPassword;
                    result = this.userPwdNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'logincode':
                    checkData = this.formData.login.verCode;
                    result = this.verCodeCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;                
                /* 注册 */
                case 'registertel':
                    checkData = this.formData.register.userTelNumber;
                    result = this.userTelNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'registertelcode':
                    checkData = this.formData.register.telVerCode;
                    result = this.telVerCodeCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'registerpwd':
                    checkData = this.formData.register.userPassword;
                    result = this.userPwdNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'registerokpwd':
                    checkData = this.formData.register.okUserPassword;
                    if(checkData!==this.formData.register.userPassword) {                        
                        let res = {
                            status: false,
                            message: '输入的两次密码不一致'
                        }
                        this.setDialogMessage(res);                       
                    }else{
                        result = this.userPwdNumCheck(checkData);
                        if(!result.status){
                            this.setDialogMessage(result);
                        }else{
                            this.setDialogMessage(result);
                        }
                    }                    
                    break;

                /* 密码找回 */
                case 'changepwdtel':
                    checkData = this.formData.forgetPwd.userTelNumber;
                    result = this.userTelNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'changepwdtelcode':
                    checkData = this.formData.forgetPwd.telVerCode;
                    result = this.telVerCodeCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'changepwdpwd':
                    checkData = this.formData.forgetPwd.userPassword;
                    result = this.userPwdNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'changepwdokpwd':
                    checkData = this.formData.forgetPwd.okUserPassword;
                    if(checkData!==this.formData.forgetPwd.userPassword) {                        
                        let res = {
                            status: false,
                            message: '输入的两次密码不一致'
                        }
                        this.setDialogMessage(res);                       
                    }else{
                        result = this.userPwdNumCheck(checkData);
                        if(!result.status){
                            this.setDialogMessage(result);
                        }else{
                            this.setDialogMessage(result);
                        }
                    }                    
                    break;
                default: 
                    break;
            }
        },
        /* 设置对话框的状态及消息 */
        setDialogMessage(obj) {
            this.pagestatus.messageinfo.ishow = !obj.status;
            this.pagestatus.messageinfo.value = obj.message;
        },
        /* 设置当前活动的个人中心二级菜单 */
        setCurrentSecondNav(csn) {
            this.$store.state.pageStatus.personCenter.currentSecondNav = csn;
        }       
    }    
};
</script>

<style lang='scss'>
#header{
    background-color: rgba(38,38,69,1);
    width:100%;
    height:50px;
    font-size: 16px;
    /* 头部菜单栏 */
    header{
        width: 1550px;
        margin: 0 auto;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
        color: #fff;

        .header-logo{
            width: 60px;
            height: 30px;
        }

        nav.header-navlist{
            width: 80%;
            margin-left: 30px;
            ul.header-nav{
                display: flex;
                flex-direction: row;
                justify-content: left;

                li{
                    margin: 0 30px;
                    letter-spacing: 1px;
                    align-self: center;

                    &.menu-actived::after{
                        content: '';
                        position: relative;
                        top: 6px;
                        left: 50%;
                        margin-left: -30px;
                        width: 60px;
                        display: block;
                        border-bottom: 4px solid #4F74FF;
                        border-radius: 2px;
                    }

                    &:hover::after{
                        content: '';
                        position: relative;
                        top: 6px;
                        left: 50%;
                        margin-left: -30px;
                        width: 60px;
                        display: block;
                        border-bottom: 4px solid #4F74FF;
                        border-radius: 2px;
                    }

                    a{
                        color: #fff;
                    }
                }
            }
        }

        div.login-register{
            position: relative;
            display: flex;
            flex-direction: column;       
            /* 未登录 */
            .isLogin-false{
                display: flex;
                flex-direction: row;
                >div{
                    width:60px;
                    height:30px;
                    line-height: 30px;
                    text-align: center;
                    letter-spacing: 2px;;
                    border: 1px solid #fff;
                    border-radius: 5px;
                    padding: 0 5px;
                    margin: 0 10px;
                    font-size: 14px;
                    &:hover{
                        background-color: #4F74FF;
                        border-color: #4F74FF;
                        cursor: pointer;
                    }
                }
            }

            /* 登录 */
            div.isLogin-true{
                display: flex;
                flex-direction: row;
                align-items: center;
                >div{
                    &.username{
                        font-size: 14px;
                    }
                    &.userlogo{                        
                        margin-left: 10px;
                        width: 40px;
                        height: 40px;
                        img{
                           border-radius: 50%; 
                        }
                    }
                }                
            }
            ul.isLogin-true{
                position: absolute;
                display: none;
                flex-direction: column;
                align-items: center;
                width: 120px;
                right: 0;
                top: 20px;
                background-color: #292951;
                margin: 0;
                padding: 5px 0;
                font-size: 14px;

                li{                                               
                    overflow: hidden;                        
                    padding: 10px 14px;
                    width: 100%;
                    text-align: center;
                    &.usermenu{
                        display: flex;
                        flex-direction: row; 
                        align-items: center;
                    }
                    span{
                        width: 12px;
                        height: 12px;
                        margin-right: 10px;
                    }                      
                    p:first-child{
                        width: fit-content;
                    }
                    p:last-child{
                        margin-top: 5px;
                        font-size: 12px;
                        color: #FF4141;
                        float: left;
                        &::after{
                            content: ' ';
                            display: block;
                            clear: both;
                            visibility: hidden;
                            height:0;
                        }
                    }
                    
                }
                li.usermenu{

                    &:hover{
                        background-color: #6973B2;
                    }
                }
                
            }
            .nav-info:hover{
                &+.menu-info{
                    display: flex;
                }
            }
            .menu-info:hover{
                display: flex;
            }
        }
    }    
}

/* 对话框 */
.dialog-container{
    /* 外容器 */
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(7, 5, 3, 0.3);
    /* 登录注册内容器 */
    .dialog-inner-container{
        width: 340px;
        margin: auto;
        position: absolute;
        top: 50%; left: 50%;
        -webkit-transform: translate(-50%,-50%);
        -ms-transform: translate(-50%,-50%);
        transform: translate(-50%,-50%);
        background-color: #fff;
        border-radius: 6px;
        padding: 20px 20px;            
    }
}

/* 对话框内容区域 */
.dialog-box{
    display: flex;
    flex-direction: column;
    align-items: left;

    /* 对话导航栏 */
    .dialog-title{
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        width: 100%;                   

        nav{
            align-self: center;
            display: inline-block;
            margin: 0 16px 20px 0;               
            font-weight: 600;
            width: fit-content;
            letter-spacing: 2px;
            text-align: center;
            color: #A3A5B5;
            font-size: 16px;
            
            &.nav-actived{
                color: #292951;
                font-size: 20px;                    
                padding-bottom: 6px;
                border-bottom: 4px solid #4F74FF;
                border-radius: 4px;
            }
            &:hover{
                cursor: pointer;
            }
        }
    }

    /* 对话内容 */
    .dialog-content{                  
        /* 表单公共样式 */
        form{
            display: flex;
            flex-direction: column;
            input{
                font-size: 16px;
                padding: 14px;
                color: rgb(135, 135, 141);
                background-color: #EDF1FF;
                border-radius:5px;
                &::-webkit-input-placeholder{
                    color: #A3A5B5;
                    font-size: 14px;
                }                    
            }
            >input{
                width: 100%;
                margin-bottom: 10px;
            }
            /* 自定义input行集元素 */
            >div.input-item{
                display: flex;
                flex-direction: row;
                align-items: center;                            
                margin-bottom: 10px;
            }
            /* 表单消息反馈 */
            >div.message{
                color: #FF4141;
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 1px;
                text-align: center;
                &::before{
                    content: '!';
                    text-align: center;
                    font-weight: normal;
                    display: inline-block;
                    width: 16px;
                    height: 16px;
                    font-size: 14px;
                    color: #fff;
                    background-color: #FF4141;
                    margin-right: 6px;
                    padding: 1px;
                    border-radius: 50%;
                }
            }

            input[type=button]{
                color: rgba(79, 117, 255, 0.8);
                font-size: 14px;
                background: none;
                padding: 0;
                &:hover{
                    cursor: pointer;
                }
            }
            input[type=submit]{
                color: #fff;
                background-color: #4F74FF;
                font-size: 16px;
                letter-spacing: 10px;
                text-align: center;
                &:hover{
                    cursor: pointer;
                }
            }
        }
        /* 登录验证码 */
        .login-vercode{
            font-size: 10px;                           
            input:first-child{
                width: 80px; 
            }
            input:last-child{
                color: rgba(80, 120, 250, 0.7);
                font-size: 14px;
                background: none;
                padding: 0;
                align-self: flex-end;
                &:hover{
                    cursor: pointer;
                }
            }
            .vercode-img{
                margin: 0 10px;
                width: 110px;
                height: 40px;
                line-height: 50px;
                box-shadow: 4px 4px 6px #EDF1FF;
                border-radius: 6px;
            }
        }
        /* 登录其他信息 */
        .login-otherinfo{
            justify-content: space-between;
            font-size: 14px;
            padding-right: 20px;
            .checkbox {
                display: flex;
                flex-direction: row;
                align-items: center;
                                                

                input[type=checkbox]{
                    appearance: none;
                    -webkit-appearance: none;
                    display: none;                                    
                                                
                }
                input[type=checkbox] + i{
                    margin-right: 5px;
                    width: 20px;
                    height: 20px;
                    background: none;
                    border-radius: 50%;
                    border:2px solid rgba(80, 120, 250, 0.6);
                    &:hover{
                        cursor: pointer;
                    }
                }
                input[type=checkbox]:checked + i{
                    display: block;
                    width: 20px;
                    height: 20px;
                    border: none;
                    background: url('../assets/img/header/select@2x.png') no-repeat center /100% 100%;
                }
            }   
        }
        /* 手机验证码按钮 */
        .vercode{                               
            input[type=text]{
                width: 100%;
            }                
            input[type=button]{
                position: absolute;
                right: 30px;                                      
                font-size: 14px;
                background-color: transparent;
                color: #4F74FF;
                height: 40px;                    
                padding: 0 10px;
                letter-spacing: .5px;
            }
        }
        /* 注册同意阅读表单 */
        .reg-text{
            margin: 0 auto;
            letter-spacing: 1px;
            /* padding-left: 20px; */
            p{
                font-size: 12px;
                color: #A3A5B5;
            }
            a{
                color: #4F74FF;
                font-size: 12px;
                letter-spacing: 0;
            }
        }
    }
    /* 对话框取消 */
    .dialog-close{
        position: absolute;
        top: 2px;
        right: 2px;
        background-color: #A3A5B5;
        border-radius: 50%;
        box-shadow: 2px 2px 4px rgb(191, 191, 241);
        padding: 2px;
        color: #fff;
        width: fit-content;
        &:hover{
            cursor: pointer;
        }
    }
}
</style>
