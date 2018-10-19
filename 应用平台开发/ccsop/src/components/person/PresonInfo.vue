<template>
    <div id="person-info">
        <div class="person-info-content">
            <!-- 小导航 -->
            <div class="nav-menu person-info-nav">
                <div :class="{'menu-item':true,'selected-item': getcurrentSecondNav =='PresonInfo-baseinfo'}"
                @click="setMenuItem('PresonInfo-baseinfo')" >
                    基本资料
                </div>
                <div :class="{'menu-item':true,'selected-item': getcurrentSecondNav =='PresonInfo-authenticate'}"
                @click="setMenuItem('PresonInfo-authenticate')">
                    实名认证
                </div>
            </div>
            <!-- 基本资料 -->
            <div class="person-info-base" v-if=" getcurrentSecondNav == 'PresonInfo-baseinfo' ">
                <form action="" method="post">
                    <div class="input-item">
                        <label for="">昵称</label>
                        <input type="text" name="username" id="username" disabled v-model="userBaseInfo.userNickName">
                        <span class="fa fa-pencil" v-if="getStatusChangingBaseInfo" @click="isOpenDialogWithType('changeUserName')"></span>
                    </div>
                    <div class="input-item">
                        <label for="">手机</label>
                        <input type="text" name="usertel" id="usertel" disabled v-model="userBaseInfo.userTel">
                        <span class="fa fa-pencil" v-if="getStatusChangingBaseInfo" @click="isOpenDialogWithType('changeTelOrEmail','changeTel')"></span>
                    </div>
                    <div class="input-item">
                        <label for="">邮箱</label>
                        <input type="text" name="useremail" id="useremail" disabled v-model="userBaseInfo.userEmail">
                        <span class="fa fa-pencil" v-if="getStatusChangingBaseInfo" @click="isOpenDialogWithType('changeTelOrEmail','changeEmail')"></span>
                    </div>
                    <div class="input-item">
                        <label for="">密码</label>
                        <input type="password" name="userpwd" id="userpwd" disabled v-model="userBaseInfo.userPwd">
                        <span class="fa fa-pencil" v-if="getStatusChangingBaseInfo" @click="isOpenDialogWithType('changeUserPassword')"></span>
                    </div>
                    <div class="btn btn-change" v-if="!getStatusChangingBaseInfo">
                        <input type="button" value="修改" class="btn-type-one" @click="setStatusChangingBaseInfo(true)" >
                        
                    </div>
                    <div class="btn btn-changing" v-if="getStatusChangingBaseInfo">
                        <input type="button" value="保存" class="btn-type-one" >
                        <input type="button" value="取消" class="btn-type-two" @click="setStatusChangingBaseInfo(false)" >
                    </div>
                </form>
            </div>
            <!-- 实名认证 -->
            <div class="person-info-authenticate" v-if=" getcurrentSecondNav == 'PresonInfo-authenticate' ">
                <form action="" method="post">
                    <div class="input-item">
                        <label for="">真实姓名：</label>
                        <input type="text" name="userrealname" id="userrealname" :class="{'input-noboder-disabled':userRealInfoStatus.isChange}" 
                        :disabled="userRealInfoStatus.isChange" placeholder="请填写您的真实姓名" 
                        v-model="userRealInfo.userRealName" @blur="dataCheck('realname')">
                        <div class="message" v-if="dialogStatus.messageBoxRealName.ishow">{{dialogStatus.messageBoxRealName.value}}</div>
                    </div>
                    <div class="input-item">
                        <label for="">身份证号：</label>
                        <input type="text" name="usercardid" id="usercardid" :class="{'input-noboder-disabled':userRealInfoStatus.isChange}" 
                        :disabled="userRealInfoStatus.isChange" placeholder="请输入有效身份证件号码" 
                        v-model="userRealInfo.userCardId" @blur="dataCheck('cardidnumber')">
                        <div class="message" v-if="dialogStatus.messageBoxCardID.ishow">{{dialogStatus.messageBoxCardID.value}}</div>
                    </div>
                    <div class="input-item">
                        <label for="">居住地址：</label>
                        <input type="text" name="useraddress" id="useraddress"  :class="{'input-noboder-disabled':userRealInfoStatus.isChange}" 
                        :disabled="userRealInfoStatus.isChange" placeholder="请填写本人证件居住地址"
                        v-model="userRealInfo.userLiveAddress" @blur="dataCheck('liveaddress')">
                        <div class="message" v-if="dialogStatus.messageBoxLiveAddress.ishow">{{dialogStatus.messageBoxLiveAddress.value}}</div>
                    </div>
                    <div class="input-item input-item-cardimg" v-if="!userRealInfoStatus.isChange">
                        <label for="">证件照片：</label>
                        <div class="cardimg-content">
                            <div class="cardimg-front">
                                <img :src=IDCardPreURL @click="postCardIdImgFront" alt="" srcset="" ref='IDCardPre'>
                                <p>身份证正面</p>
                            </div>
                            <div class="cardimg-back">
                                <img :src=IDCardBackURL @click="postCardIdImgBack" alt="" srcset="" ref='IDCardBack'>
                                <p>身份证反面</p>
                            </div>
                        </div>                        
                        <input type="file"  name="cardidimgfront" id="cardidimgfront"  @change="changeImgFront($event)" ref="cardidimgfront" hidden>
                        <input type="file" name="cardidimgback" id="cardidimgback" @change="changeImgBack($event)"  ref="cardidimgback" hidden>                        
                    </div>
                    <div class="btn btn-change" v-if="!userRealInfoStatus.isChange">
                        <input type="button" value="提交验证" @click="realInfoSubmit()" class="btn-type-one" >                        
                    </div>                    
                </form>
            </div>
        </div>
        
        <!-- 对话框 -->
        <div class="dialog-container" v-if="dialogStatus.isOpenDialog" >
            <!-- 修改昵称 -->
            <div class="dialog-inner-container " v-if="dialogStatus.dialogType === 'changeUserName' ">
                <div class="dialog-box">
                    <!-- 对话导航栏 -->
                    <div class="dialog-title">
                        <nav class='nav-actived'>修改昵称</nav>                        
                    </div>
                    <!-- 对话框取消 -->
                    <div class="dialog-close" @click.stop.prevent="isOpenDialogWithType()">&nbsp;x&nbsp;</div>
                    <!-- 对话内容 -->
                    <div class="dialog-content">
                        <div class="login-content">
                            <form action="" method="post" class="form-noboder">
                                <input type="text" name="usernickname" id="usernickname" ref="usernickname"
                                 v-model="tempUserBaseInfo.userNickName"  @blur="dataCheck('change-nickname')">                         
                                <input type="submit" 
                                @click.stop.prevent="changeUserNickNameSubmit()" value="确认修改">
                                <!-- 状态消息 -->
                                <div class="message login-status" 
                                v-if="dialogStatus.messageBoxInfo.ishow">{{dialogStatus.messageBoxInfo.value}}</div>
                            </form>
                        </div>                                             
                    </div>
                </div>
            </div>

            <!--修改手机或邮箱 -->
            <div class="dialog-inner-container " v-if="dialogStatus.dialogType === 'changeTelOrEmail' ">
                <div class="dialog-box">
                    <!-- 对话导航栏 -->
                    <div class="dialog-title">
                        <nav :class="{'nav-actived':dialogStatus.changeTelToChangeEmail === 'changeTel' }" 
                        @click.stop.prevent="setChangeTelToChangeEmail('changeTel')" >修改手机</nav>
                        <nav :class="{'nav-actived':dialogStatus.changeTelToChangeEmail === 'changeEmail' }" 
                        @click.stop.prevent="setChangeTelToChangeEmail('changeEmail')">修改邮箱</nav>
                    </div>
                    <!-- 对话框取消 -->
                    <div class="dialog-close" @click.stop.prevent="isOpenDialogWithType()">&nbsp;x&nbsp;</div>
                    <!-- 对话内容 -->
                    <div class="dialog-content">
                        <!-- 修改手机 -->
                        <div class="login-content" v-if="dialogStatus.changeTelToChangeEmail === 'changeTel'">
                            <form action="" method="post">
                                <div class="input-item vercode vercode-tel">
                                    <input type="text" name="oldtelcode" id="oldtelcode" placeholder="原手机短信验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>
                                <input type="text" name="newtelnumber" id="newtelnumber" ref="newtelnumber"  placeholder="新手机号"
                                 v-model="tempUserBaseInfo.userTel" @blur="dataCheck('telnumber')">
                                <div class="input-item vercode vercode-tel">
                                    <input type="text" name="newtelcode" id="newtelcode" placeholder="新手机短信验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>                              
                                <input type="submit" @click.stop.prevent="changeUserTelSubmit()" value="确认修改">
                                <!-- 状态消息 -->
                                <div class="message login-status" 
                                v-if="dialogStatus.messageBoxInfo.ishow">{{dialogStatus.messageBoxInfo.value}}</div>
                            </form>
                        </div>
                        <!-- 修改邮箱 -->
                        <div class="register-content" v-if="dialogStatus.changeTelToChangeEmail === 'changeEmail' ">
                            <form action="" method="post">
                                <div class="input-item vercode vercode-email">
                                    <input type="text" name="oldemailcode" id="oldemailcode" placeholder="原邮箱验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>
                                <input type="text" name="newemailnumber" id="newemailnumber" ref="newemailnumber"  placeholder="新邮箱号"
                                 v-model="tempUserBaseInfo.userEmail" @blur="dataCheck('emailnumber')" >
                                <div class="input-item vercode vercode-email">
                                    <input type="text" name="newemailcode" id="newemailcode" placeholder="新邮箱验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>                              
                                <input type="submit" @click.stop.prevent="changeUserEmailSubmit()" value="确认修改">
                                <!-- 状态消息 -->
                                <div class="message login-status"
                                v-if="dialogStatus.messageBoxInfo.ishow">{{dialogStatus.messageBoxInfo.value}}</div>
                            </form>            
                        </div>                        
                    </div>
                </div>
            </div>

            <!-- 修改密码 -->
            <div class="dialog-inner-container " v-if="dialogStatus.dialogType === 'changeUserPassword' ">
                <div class="dialog-box">
                    <!-- 对话导航栏 -->
                    <div class="dialog-title">
                        <nav :class="{'nav-actived':dialogStatus.wayOfChangePwd === 'telChangePwd' }" 
                        @click.stop.prevent="setWayOfChangePwd('telChangePwd')" >手机改密</nav>
                        <nav :class="{'nav-actived':dialogStatus.wayOfChangePwd === 'emailChangePwd' }" 
                        @click.stop.prevent="setWayOfChangePwd('emailChangePwd')">邮箱改密</nav>
                    </div>
                    <!-- 对话框取消 -->
                    <div class="dialog-close" @click.stop.prevent="isOpenDialogWithType()">&nbsp;x&nbsp;</div>
                    <!-- 对话内容 -->
                    <div class="dialog-content">
                        <!-- 手机修改 -->
                        <div class="login-content" v-if=" dialogStatus.wayOfChangePwd === 'telChangePwd' ">
                            <form action="" method="post">
                                <div class="input-item vercode vercode-tel">
                                    <input type="text" name="oldtelcode" id="oldtelcode" placeholder="原手机号验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>
                                <input type="password" name="newpassword" id="newpassword"  ref="newpassword" placeholder="新密码"
                                 v-model="tempUserBaseInfo.userPwd" @blur="dataCheck('password')">
                                <input type="password" name="oknewpassword" id="oknewpassword"  placeholder="确认新密码"
                                 v-model="tempUserBaseInfo.okUserPwd" @blur="dataCheck('okpassword')" >                             
                                <input type="submit" @click.stop.prevent="changeUserPwdSubmit()" value="确认修改">
                                <!-- 状态消息 -->
                                <div class="message login-status" 
                                v-if="dialogStatus.messageBoxInfo.ishow">{{dialogStatus.messageBoxInfo.value}}</div>
                            </form>
                        </div>
                        <!-- 邮箱修改 -->
                        <div class="register-content" v-if=" dialogStatus.wayOfChangePwd === 'emailChangePwd' ">
                            <form action="" method="post">
                                <div class="input-item vercode vercode-email">
                                    <input type="text" name="oldemailcode" id="oldemailcode" placeholder="原邮箱验证码"
                                    >
                                    <input type="button" @click.stop.prevent="" value="获取验证码">
                                </div>
                                <input type="password" name="newpassword" id="newpassword" ref="newpassword"  placeholder="新密码"
                                 v-model="tempUserBaseInfo.userPwd" @blur="dataCheck('password')" >
                                <input type="password" name="oknewpassword" id="oknewpassword"  placeholder="确认新密码"
                                 v-model="tempUserBaseInfo.okUserPwd" @blur="dataCheck('okpassword')" >                             
                                <input type="submit" @click.stop.prevent="changeUserPwdSubmit()" value="确认修改">
                                <!-- 状态消息 -->
                                <div class="message login-status"
                                v-if="dialogStatus.messageBoxInfo.ishow">{{dialogStatus.messageBoxInfo.value}}</div>
                            </form>            
                        </div>                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import IDCardPreURL from "@/assets/img/personinfo/card-front.png"
import IDCardBackURL from "@/assets/img/personinfo/card-back.png"
export default {
    data() {
        return {
            userBaseInfo: {
                userNickName: this.$store.state.publicData.userinfo.userNickName,
                userTel: this.$store.state.publicData.userinfo.userCount,
                userEmail: this.$store.state.publicData.userinfo.userEmail,
                userPwd: '************'
            },
            tempUserBaseInfo: {
                userNickName: this.$store.state.publicData.userinfo.userNickName,
                userTel: '',
                userEmail: '',
                userPwd: '',
                okUserPwd: ''
            },
            userRealInfo: {
                userRealName: '',
                userCardId: '',
                userLiveAddress: ''
            },
            /* 用户真是信息状态 */
            userRealInfoStatus: null,
            /* 页面状态量 */            
            dialogStatus:{
                isOpenDialog: false,
                dialogType: 'changeUserName',
                changeTelToChangeEmail: 'changeTel',
                wayOfChangePwd: 'telChangePwd',
                messageBoxInfo: {ishow: false ,value: '出错，请刷新网页重新操作'},
                messageBoxRealName: {ishow: false ,value: '姓名格式错误'},
                messageBoxCardID: {ishow: false ,value: '身份证号格式错误'},
                messageBoxLiveAddress: {ishow: false ,value: '居住地址格式错误'},
            },
            IDCardPreURL,//正面身份证信息
            IDCardBackURL//反面身份证信息            
        }
    },
    computed: {
        getcurrentSecondNav() {
            return this.$store.state.pageStatus.personCenter.currentSecondNav;
        },
        getStatusChangingBaseInfo() {
            return this.$store.state.pageStatus.presonInfo.isChangingBaseInfo;
        },
        getUserRealInfoStatus() {
            
            return this.$store.getters.getUserRealInfoState;
        } 
    },
    methods: {
        setMenuItem(go) {
            let isChangingBaseInfo = this.$store.state.pageStatus.presonInfo.isChangingBaseInfo;
            /* 如果资料处于修改状态 */
            if(isChangingBaseInfo){
                if(confirm('您正在修改个人资料，确定撤销修改？')){
                    this.$store.state.pageStatus.personCenter.currentSecondNav = go;
                    this.$store.state.pageStatus.presonInfo.isChangingBaseInfo = false;
                    return ;
                }else{
                    return ;
                }
            }
            this.$store.state.pageStatus.personCenter.currentSecondNav = go;
        },
        setStatusChangingBaseInfo(state){
           this.$store.state.pageStatus.presonInfo.isChangingBaseInfo = state;
        },
        /* 设置对话框状态 */
        isOpenDialogWithType(type,other) {
            if(type && other){
                this.dialogStatus.messageBoxInfo.ishow = false;
                this.dialogStatus.isOpenDialog = true;
                this.dialogStatus.dialogType = type;
                this.dialogStatus.changeTelToChangeEmail = other;
            }else if(type){
                this.dialogStatus.messageBoxInfo.ishow = false;
                this.dialogStatus.isOpenDialog = true;
                this.dialogStatus.dialogType = type;
                this.dialogStatus.changeTelToChangeEmail = null;
            }else{
                this.dialogStatus.messageBoxInfo.ishow = false;
                this.dialogStatus.isOpenDialog = false;
                this.dialogStatus.dialogType = null;
                this.dialogStatus.changeTelToChangeEmail = null;
            }
        },
        setChangeTelToChangeEmail(type) {
            if(type) {
                this.dialogStatus.messageBoxInfo.ishow = false;
                this.dialogStatus.changeTelToChangeEmail = type;
            }
        },
        setWayOfChangePwd(way){
            if(way) {
                this.dialogStatus.messageBoxInfo.ishow = false;
                this.dialogStatus.wayOfChangePwd = way;
            }else{

            }
        },
        /* 对话框确认按钮提交 */
        changeUserNickNameSubmit() {
            let checkData = this.tempUserBaseInfo.userNickName.trim();
            let checkResult = this.userNickNameCheck(checkData);
            if(checkResult.status){
                this.userBaseInfo.userNickName = checkData;
                this.dialogStatus.isOpenDialog = false;
                this.dialogStatus.value = '';
            }            
        },
        changeUserTelSubmit() {
            let checkData = this.tempUserBaseInfo.userTel.trim();
            let checkResult = this.userTelNumCheck(checkData);
            if(checkResult.status){
                this.userBaseInfo.userTel = checkData;
                this.tempUserBaseInfo.userTel = '';
                this.dialogStatus.isOpenDialog = false;
                this.dialogStatus.value = '';
            }            
        },
        changeUserEmailSubmit() {
            let checkData = this.tempUserBaseInfo.userEmail.trim();
            let checkResult = this.userEmailNumCheck(checkData);
            if(checkResult.status) {
                this.userBaseInfo.userEmail = checkData;
                this.tempUserBaseInfo.userEmail = '';
                this.dialogStatus.isOpenDialog = false;
                this.dialogStatus.value = '';
            }
        },
        changeUserPwdSubmit() {
            let checkData1 = this.tempUserBaseInfo.userPwd.trim();
            let checkResult1 = this.userPwdNumCheck(checkData1);
            let checkData2 = this.tempUserBaseInfo.okUserPwd.trim();
            let checkResult2 = this.userPwdNumCheck(checkData2);
            if(checkData1!==checkData2){
                let res = {
                        status: false,
                        message: '输入的两次密码不一致'
                    }
                this.setDialogMessage(res);
                return ;
            }
            if(checkResult1.status && checkResult2.status) {
                this.userBaseInfo.userPwd = checkData1;
                this.tempUserBaseInfo.userPwd = '';
                this.tempUserBaseInfo.okUserPwd = '';
                this.dialogStatus.isOpenDialog = false;
                this.dialogStatus.value = '';
            }
        },
        /* 真实信息验证提交 */
        realInfoSubmit() {            
            if(!this.dialogStatus.messageBoxRealName.ishow && !this.dialogStatus.messageBoxCardID.ishow && !this.dialogStatus.messageBoxLiveAddress.ishow){
                let cardidimgfront = this.$refs.cardidimgfront;
                let cardidimgback = this.$refs.cardidimgback;
                
                /* let checkRelust =this.realIdCardImgCheck(checkObj); */
                if(cardidimgfront.files.length<=0){
                    alert('请上传身份证正面照片');
                }else if(cardidimgback.files.length<=0) {
                    alert('请上传身份证背面照片');
                }else{

                    return true;
                }
            }else{
                alert("请检查您的信息输入格式并正确输入！")
            }
        },
        /* 表单数据验证 */
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
        /* 邮箱号正则 */
        userEmailNumCheck(num) {
            if(!num) {
                return {
                    status: false,
                    message: "请输入您的邮箱"
                }
            }
            let regex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
            if(!regex.test(num)){
                return {
                    status: false,
                    message: '请正确输入邮箱'
                }
            }else{
                return {
                    status: true,
                    message: '邮箱验证成功'
                }
            }
        },
        /* 昵称正则 */
        userNickNameCheck(num) {
            /* 规则：2-8个任意字符  只含有汉字、数字、字母、下划线不能以下划线开头和结尾*/
            if(!num) {
                return {
                    status: false,
                    message: "请输入您的昵称"
                }
            }
            let regex = /^(?!_)(?!.*?_$)([a-zA-Z0-9_\u4e00-\u9fa5]{2,8})$/;
            if(!regex.test(num)){
                return {
                    status: false,
                    message: '请正确输入2-8个字符的手机昵称'
                }
            }else{
                return {
                    status: true,
                    message: '昵称验证成功'
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
                    message: "请输入发送至您手机的验证码"
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
                    message: '验证码验证成功'
                }
            }       
        },
        /* 邮箱验证码正则 */
        emailVerCodeCheck(num) {
            /* 规则：4位纯数字 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入发送至您邮箱号的验证码"
                }
            }           
            let regex = /^\d{4}$/;
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
        /* 实名认证 姓名验证 */
        realNameCheck(num) {
            /* 规则：2-8位中文 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入姓名"
                }
            }            
            let regex = /^[\u4e00-\u9fa5]{2,8}$/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请输入正确的姓名'
                }
            }else{
                return {
                    status: true,
                    message: '姓名验证成功'
                }
            }
        },
        /* 实名认证 身份证号认证 */
        realCardIdNumberCheck(num) {
            /* 规则：18位纯数字; 17位数字，第十八位是'X'; 17位数字，第十八位是'x' */
            if(!num) {
                return {
                    status: false,
                    message: "请输入身份证号"
                }
            }            
            let regex = /(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请输入正确的身份证号'
                }
            }else{
                return {
                    status: true,
                    message: '身份证号验证成功'
                }
            }
        },
        /* 实名认证 地址验证 */
        realLiveAddressCheck(num) {
            /* 规则：非空 */
            if(!num) {
                return {
                    status: false,
                    message: "请输入地址"
                }
            }else{
                return {
                    status: true,
                    message: '地址验证成功'
                }
            }
        },
        /* 实名认证 身份证照片验证 */
        realIdCardImgCheck(num) {
            /* 规则：图片长度 */
            if(!num) {
                return {
                    status: false,
                    message: "请上传所需图片"
                }
            }            
            let regex = /^[\u4e00-\u9fa5]{2,8}$/;
            if(!regex.test(num)) {
                return {
                    status: false,
                    message: '请上传规定规格的图片'
                }
            }else{
                return {
                    status: true,
                    message: '图片验证成功'
                }
            }
        },
        /* 数据检查dataCheck */
        dataCheck(type) {
            /* type类： 手机号telnumber 密码password 手机验证码telvercode  邮箱验证码emailvercode
                昵称change-nickname  邮箱emailnumber 真实姓名 realname 身份证号 cardidnumber  居住地址 address
            */
            let checkData = null,result = null;
            switch (type) {                
                case 'telnumber':
                    checkData = this.tempUserBaseInfo.userTel.trim();
                    result = this.userTelNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;               
                case 'emailnumber':
                    checkData = this.tempUserBaseInfo.userEmail.trim();
                    result = this.userEmailNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'change-nickname':
                    checkData = this.tempUserBaseInfo.userNickName.trim();
                    result = this.userNickNameCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'password':
                    checkData = this.tempUserBaseInfo.userPwd.trim();
                    result = this.userPwdNumCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                 case 'okpassword':
                     checkData = this.tempUserBaseInfo.userPwd.trim();
                    if(checkData!==this.tempUserBaseInfo.okUserPwd.trim()) {                        
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
                case 'telvercode':
                    checkData = '';
                    result = this.telVerCodeCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'emailvercode':
                    checkData = '';
                    result = this.emailVerCodeCheck(checkData);
                    if(!result.status){
                        this.setDialogMessage(result);
                    }else{
                        this.setDialogMessage(result);
                    }
                    break;
                case 'realname':
                    checkData = this.userRealInfo.userRealName;
                    result = this.realNameCheck(checkData);
                    if(!result.status){
                        this.dialogStatus.messageBoxRealName.ishow = !result.status;
                        this.dialogStatus.messageBoxRealName.value = result.message;                        
                    }else{
                        this.dialogStatus.messageBoxRealName.ishow = !result.status;
                        this.dialogStatus.messageBoxRealName.value = '';
                    }
                    break;
                case 'cardidnumber':
                    checkData = this.userRealInfo.userCardId;
                    result = this.realCardIdNumberCheck(checkData);
                    if(!result.status){
                        this.dialogStatus.messageBoxCardID.ishow = !result.status;
                        this.dialogStatus.messageBoxCardID.value = result.message;
                    }else{
                        this.dialogStatus.messageBoxCardID.ishow = !result.status;
                        this.dialogStatus.messageBoxCardID.value = '';
                    }
                    break;
                case 'liveaddress':
                    checkData = this.userRealInfo.userLiveAddress;
                    result = this.realLiveAddressCheck(checkData);
                    if(!result.status){
                        this.dialogStatus.messageBoxLiveAddress.ishow = !result.status;
                        this.dialogStatus.messageBoxLiveAddress.value = result.message;
                    }else{
                        this.dialogStatus.messageBoxLiveAddress.ishow = !result.status;
                        this.dialogStatus.messageBoxLiveAddress.value = '';
                    }
                    break;                
                default: 
                    break;
            }
        },
        /* 设置对话框的状态及消息 */
        setDialogMessage(obj) {
            this.dialogStatus.messageBoxInfo.ishow = !obj.status;
            this.dialogStatus.messageBoxInfo.value = obj.message;
        },
        postCardIdImgFront(){
            this.$refs.cardidimgfront.click();
        },
        /* 上传身份证正面 */
        changeImgFront(event) {
            let files = this.$refs.cardidimgfront.files[0];
            if(files!=null){
                var reader = new FileReader();//读取文件内容
                reader.readAsDataURL(files);
                let _this = this;
                reader.onload = function() {
                    if(files.type==='image/png'||files.type==='image/jpeg'){
                        if(files.size<=102400){ //图片大小在5kb-0.5kb之间
                            if(files.size>=512){
                                _this.$refs.IDCardPre.src = this.result;
                            }else{
                                alert("图片太小")
                            }
                        }else{
                            alert("图片太大")
                        }
                    }else{
                        alert("图片格式不正确")
                    }
                }
            }
        },
        postCardIdImgBack(){
            this.$refs.cardidimgback.click();
        },
        /* 上传身份证反面 */
        changeImgBack(event){
            let filesBack = this.$refs.cardidimgback.files[0];
            console.log(filesBack)
                if(filesBack!=null){
                var reader = new FileReader();//读取文件内容
                reader.readAsDataURL(filesBack);
                let _this = this;
                reader.onload = function() {
                    if(filesBack.type==='image/png'||filesBack.type==='image/jpeg'){
                        if(filesBack.size<=102400){ //图片大小在5kb-0.5kb之间
                            if(filesBack.size>=512){
                                _this.$refs.IDCardBack.src = this.result;
                            }else{
                                alert("图片太小")
                            }
                        }else{
                            alert("图片太大")
                        }
                    }else{
                        alert("图片格式不正确")
                    }
                }
            }

        }
    },
    mounted() {
        this.userRealInfoStatus = this.getUserRealInfoStatus;
        this.userRealInfo.userRealName = this.getUserRealInfoStatus.msg.userRealName;
        this.userRealInfo.userCardId = this.getUserRealInfoStatus.msg.userCardId;
        this.userRealInfo.userAddress = this.getUserRealInfoStatus.msg.userAddress;
        /* console.log(this.getUserRealInfoStatus);  */
    },    
    created() {        
    },
    /* watch:{
        '$route.query': function(newVal,oldVal) {
           this.$store.state.pageStatus.personCenter.currentSecondNav = newVal.menu;
        }
    } */
}
</script>

<style lang="scss">
#person-info{
    width: 100%;
    .person-info-content{
        display: flex;
        flex-direction: column;
        width: 100%;
        .nav-menu{
            display: flex;
            flex-direction: row;
            width: 100%;
            height: 80px;
            border-bottom: 2px solid #EDEDF0;
            line-height: 80px;
            font-size: 18px;
            .menu-item{
                margin-left: 60px;
                &.selected-item{
                    color: #4F74FF;
                    border-bottom:4px solid #4F74FF;
                    border-radius: 2px;
                }
            }
        }
        /* 公共表单 */
        form{
            display: flex;
            flex-direction: column;
            font-size: 18px;
            color: #383849;
            font-size: 18px;
            input:disabled{
                background: none;
            }
            .input-item{
                display: flex;
                flex-direction: row;
                align-items: center;
                margin-bottom: 60px;
                label{
                    margin-right: 60px;                            
                }
                input{
                    font-size: 18px;
                    color: #383849;
                }
                .message{
                    margin-left: 20px;
                    color: #FF4141;
                    font-size: 16px;
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
            }
            .btn{
                input[type=button] {                        
                    font-size: 18px;                            
                    width:120px;
                    height:40px;
                    border-radius:20px;
                    &.btn-type-one{
                        color:#fff;
                        background-color: #4F74FF;
                    }
                    &.btn-type-two{
                        color:#4F74FF;
                        background-color: #fff;
                        border: 1px solid #4F74FF;
                        margin-left: 30px;
                    }
                    &:hover{
                        cursor: pointer;
                    }
                }
            }       
        } 
        /* 基本资料 */
        .person-info-base{
            margin-top: 100px;
            margin-left: 60px;
            .fa-pencil{                
                &:hover{                   
                    display: inline-block;
                    border: 2px dashed #4F74FF;
                    cursor: pointer;
                }
            }
        }

        /* 实名认证 */
        .person-info-authenticate{
            margin-top: 100px;
            margin-left: 60px;

            form{
                input{
                    border: 1px solid #D8D8D8;
                    border-radius:5px;
                    height: 50px;
                    width: 440px;
                    &[type=text]{
                        padding-left: 20px;
                    }
                    &::-webkit-input-placeholder{
                    color: #A0A0A8;
                    font-size: 16px;
                    }
                    &.input-noboder-disabled{
                        border: none;
                        background: none;
                    }
                }
                .input-item-cardimg{
                    display: flex;
                    flex-direction: row;
                    .card1{
                        opacity: 0.2;
                        height: 120px;
                        width: 190px;
                        transform: translateY(-153px);
                    }
                }
                .cardimg-content{
                    display: flex;
                    flex-direction: row;
                    justify-content: space-between;
                    width: 440px;
                    >div{
                        width: 190px;
                        height: 120px;
                        text-align: center;
                        color: #B9B9BF;
                        img{
                            border-radius: 10px;
                        }
                    }
                }
            }
        }
        
    }

}
</style>
