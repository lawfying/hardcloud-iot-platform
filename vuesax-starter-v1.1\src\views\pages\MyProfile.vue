<template>
        <div>
          <div class="flex flex-wrap">
            <div class="w-full">
                <vs-row vs-justify="center" >
                <div class="con-img ml-3"><img :src=url+myprofile.mugshot  alt="" width="200" height="200" class="rounded-full shadow-md cursor-pointer block"></div>
                </vs-row>
                <br>
                <div class="w-full">
                <h5 style="text-align:center;"><span class="text-success" > 欢迎您：{{ myprofile.username }} </span></h5>
                </div> 
                <br>
            </div>
            
             <div class="w-full">
             <vx-card class="overlay-card overflow-hidden">
            <vs-row>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="2">
                 <h5  class="text-success" >登录密码 </h5>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="6">
                <span> 建议设置包含字母，符号或数字中至少两项且长度超过6位的密码。</span>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="4">
                <vs-button color="success" type="flat" icon-pack="feather" icon="icon-edit" @click="popupActivePassword_updatefunc()">修改</vs-button>
                <vs-popup class="holamundo"  title="修改密码" :active.sync="popupActivePassword_update" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     新设置密码：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" type="password" v-model="newpassword1"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12"> <br> </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     重新输入密码：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" type="password" v-model="newpassword2"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12"> <br> </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="password_update()">更新</vs-button>
                                    </vs-col>
                                   
                </vs-popup>
            </vs-col>
            </vs-row>
            
            <vs-divider/>
             <vs-row>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="2">
                 <h5  class="text-success" >电话号码</h5>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="6">
                <span> 您的电话号码：{{ myprofile.phone_num }}。</span>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="4">
                <vs-button color="success" type="flat" icon-pack="feather" icon="icon-edit" @click="popupActivePhonenum_updatefunc(myprofile.myprofile_id)">修改</vs-button>
                <vs-popup class="holamundo"  title="修改电话号码" :active.sync="popupActivePhonenum_update" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     新电话号码：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="newphonenum"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12"> <br> </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="phonenum_update()">更新</vs-button>
                                    </vs-col>
                                   
                </vs-popup>
            </vs-col>
            </vs-row>
            <vs-divider/>
            <vs-row>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="2">
                 <h5  class="text-success" >用户头像</h5>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="6">
                 <span> 修改头像。</span>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="4">
                <vs-button color="success" type="flat" icon-pack="feather" icon="icon-edit"  @click="popupActiveMugshot_updatefunc(myprofile.myprofile_id)">修改</vs-button>
                <vs-popup class="holamundo"  title="修改头像" :active.sync="popupActiveMugshot_update" background-color="rgba(0,0,0,.1)">
                                    <div class="vx-col w-full" >
                                    <p class="vs-input--label"> 更新头像</p>
                                    <input type="file" @change="triggerFile($event)" class="w-full vs-input--input">
                                    </div>
                                    <div class="vx-row" style="margin-top:20px">
                                    </div>

                                    <div class="vx-row mb-6 w-5/6 ">
                                    <img :src=url+myprofile.mugshot alt="content-img" style="margin-left:10px;"  class="responsive rounded-lg">
                                    </div>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12"> <br> </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="mugshot_update()">更新</vs-button>
                                    </vs-col>
                                   
                </vs-popup>
            </vs-col>
            </vs-row>
            <vs-divider/>
            <vs-row>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="2">
                 <h5  class="text-success" >邮箱</h5>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="6">
                <span> 您的邮箱：{{ myprofile.email }}，可以通过邮箱重置密码。</span>
            </vs-col>
            <!-- <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="4">
                <vs-button color="success" type="flat" icon-pack="feather" icon="icon-edit" @click="popupActiveEmail_updatefunc()">修改</vs-button>
                <vs-popup class="holamundo"  title="修改电话号码" :active.sync="popupActivePhonenum_update" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     新电话号码：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="newphonenum"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12"> <br> </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="phonenum_update()">更新</vs-button>
                                    </vs-col>
                                   
                </vs-popup>
            </vs-col> -->
            <!-- <vs-col v-tooltip="'col - 4'" vs-type="flex"  vs-align="center"  vs-w="4">
               
            </vs-col> -->
            </vs-row>
            
           
            </vx-card>
 
            </div>

            </div>
        </div>
</template>


<script>

import {FormWizard, TabContent} from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import vSelect from 'vue-select'

export default {


  data() {
    return {
     
      myprofile:'',
      url:this.GLOBAL.baseURL,
      popupActivePassword_update:false,
      newpassword1:'',
      newpassword2:'',

      popupActivePhonenum_update:false,
      newphonenum:'',
      myprofileid:'',

      popupActiveMugshot_update:false,


      
    }
  },


  created: async function() {
      const response = await this.axios.get(this.GLOBAL.baseURL+'/rest-auth/myprofile/').catch(function (error) {
			console.log(error)
            return error.response.data;});
      if (response.status==200) {
          this.myprofile = response.data;
      }


  },

  methods:{
       triggerFile : function (event) {
  this.imgfile = event.target.files; // (利用console.log输出看结构就知道如何处理档案资料)
  // do something...
},
      popupActivePassword_updatefunc(){
          this.popupActivePassword_update = true;
      },
      async password_update(){

          var params={'new_password1':this.newpassword1,'new_password2':this.newpassword2}

        const response = await this.axios.post(this.GLOBAL.baseURL+'/rest-auth/password/change/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
        if(response.status=='200'){
               alert("修改成功");
               this.popupActivePassword_update = false;
               this.newpassword1='';
               this.newpassword2='';
            }
      },
      popupActivePhonenum_updatefunc(param){
          this.popupActivePhonenum_update=true;
          this.myprofileid = param;
          this.newphonenum = this.myprofile.phone_num;
      },
      async phonenum_update(){
          var params={'phone_num':this.newphonenum}
        const response = await this.axios.patch(this.GLOBAL.baseURL+'/rest-auth/myprofile/'+this.myprofileid+'/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
        this.myprofile.phone_num = response.data.phone_num;
        this.popupActivePhonenum_update = false;
      },
      popupActiveMugshot_updatefunc(param){
          this.popupActiveMugshot_update=true;
          this.myprofileid = param;

      },
      async mugshot_update(){

          // let file = document.getElementById("imgLocal1").files[0]
     
      let params = new FormData() // 创建form对象
      
			let config = {
				headers: {'Content-Type': 'multipart/form-data'}
                }
                if(this.imgfile[0]) {
           params.append('mugshot', this.imgfile[0],this.imgfile[0].name) // 通过append向form对象添加数据
      }
      const response = await this.axios.patch(this.GLOBAL.baseURL+'/rest-auth/myprofile/'+this.myprofileid+'/',params,config).catch(function (error) {
                    console.log(error)
            return error.response.data;});

            var tmpimg = response.data.mugshot;
            this.myprofile.mugshot = tmpimg.substring(this.url.length,tmpimg.length);
            this.popupActiveMugshot_update = false;

      },
  },



	components: {
		'v-select': vSelect,
		FormWizard,
		TabContent
	}
  


}
</script>
