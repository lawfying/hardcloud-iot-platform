<!-- =========================================================================================
	File Name: Login.vue
	Description: Login Page
	----------------------------------------------------------------------------------------
	Item Name: Vuesax Admin - VueJS Dashboard Admin Template
	Version: 1.1
	Author: Pixinvent
	Author URL: hhttp://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>
	<div class="h-screen flex w-full bg-img">
		<div class="vx-col sm:w-1/2 md:w-1/2 lg:w-3/4 xl:w-3/5 mx-auto self-center">
			<vx-card>
				<div slot="no-body" class="full-page-bg-color">
					<div class="vx-row">
						<div class="vx-col hidden sm:hidden md:hidden lg:block lg:w-1/2 mx-auto self-center">
							<img src="@/assets/images/pages/login.png" alt="login" class="mx-auto">							
						</div>
						<div class="vx-col sm:w-full md:w-full lg:w-1/2 mx-auto self-center bg-white">
							<div class="p-8">
								<div class="vx-card__title mb-8">
									<h4 class="mb-4">登录</h4>
									<p>{{message}}</p>
								</div>
								<vs-input icon="icon icon-user" icon-pack="feather" v-model="value1" class="w-full mb-6 no-icon-border"/>
								<vs-input type="password" icon="icon icon-lock" icon-pack="feather" v-model="value2" class="w-full mb-4 no-icon-border" />
								<vs-progress indeterminate color="primary" v-show="loginstatus"></vs-progress>
								<div class="flex flex-wrap justify-between my-5">
									<vs-checkbox v-model="checkBox1" class="mb-3">记住密码</vs-checkbox>
									<!-- <router-link to="/pages/forgot-password">忘记密码?</router-link> -->
									<a href="https://yingcloud.com:8000/password-reset/">忘记密码?</a>
								</div>
								<vs-button  type="border" to="/pages/register">注册</vs-button>
								<vs-button class="float-right" @click="greet()">登录</vs-button>
								

								
								<!-- <vs-divider position="center" class="my-8"></vs-divider>

								<div class="social-login mb-4 flex flex-wrap justify-between">
									<span>Or Login With</span>
									<div class="social-login-buttons flex">
										<vs-button color="#1551b1" class="mr-4 px-8" icon="icon icon-facebook" icon-pack="feather"></vs-button>
										<vs-button color="#00aaff" class="px-8" icon="icon icon-twitter" icon-pack="feather"></vs-button>
									</div>
								</div> -->
								
							</div>
						</div>
					</div>
				</div>
			</vx-card>
		</div>
	</div>
</template>

<script>

export default {
	data() {
		return {
			value1: '',
			value2: '',
			checkBox1: false,
			message: '欢迎智能物联网平台',
			loginstatus:false,
		}
	},
	
	mounted() {
	window.sessionStorage.removeItem('Authorization');
	this.getCookie();
	if(this.value1&&this.value2){this.checkBox1=true;}
  },


	methods: {

		// async greet ()  {
		// 	var params= {username:this.value1,password:this.value2}
		// 	const response = await this.axios.post(this.GLOBAL.baseURL+'/rest-auth/login/',params).catch(function (error) {
		// 		console.log(error)
		// 		return error.response.data;});
		// 	if(response.status==200) this.$router.push('/devices/templates');
			
		// 	if (response.non_field_errors) this.message = response.non_field_errors.toString();
		// 	if (response.password) this.message = response.password.toString();
		// 	if (response.username) this.message = response.username.toString();
		// 	await this.tokenFunction(params);
			
		// 	return true;

		// }

		async greet ()  {
			this.loginstatus=true;
			var params= {username:this.value1,password:this.value2}
			try {
				const response = await this.axios.post(this.GLOBAL.baseURL+'/token-api/token/',params)
			
			//alert('tokenfunction') 
			window.sessionStorage.setItem('Authorization', 'Bearer'+' '+ response.data.access)
			// window.sessionStorage.setItem('accessToken', response.data.access)
			// window.sessionStorage.setItem('refreshToken', response.data.refresh)

			if(response.status==200) this.$router.push('/dashboard');

			}
			catch {
				this.message="请重新输入用户名、密码.";
				this.loginstatus = false;

			}

			if (this.checkBox1 == true) {
				// console.log("checked == true");
				//传入账号名，密码，和保存天数3个参数
				this.setCookie(params.username,params.password, 7);
			} else {
				// console.log("清空Cookie");
				//清空Cookie
				this.clearCookie();
			}
			
			return true;

		},
	
	setCookie(c_name, c_pwd, exdays) {
      var exdate = new Date(); //获取时间
      exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays); //保存的天数
      //字符串拼接cookie
      window.document.cookie =
        "userName" + "=" + c_name + ";path=/;expires=" + exdate.toGMTString();
      window.document.cookie =
        "userPwd" + "=" + c_pwd + ";path=/;expires=" + exdate.toGMTString();
	},
	
	getCookie: function() {
      if (document.cookie.length > 0) {
        var arr = document.cookie.split("; "); //这里显示的格式需要切割一下自己可输出看下
        for (var i = 0; i < arr.length; i++) {
          var arr2 = arr[i].split("="); //再次切割
          //判断查找相对应的值
          if (arr2[0] == "userName") {
            this.value1 = arr2[1]; //保存到保存数据的地方
          } else if (arr2[0] == "userPwd") {
            this.value2 = arr2[1];
          }
        }
      }
	},
	
	clearCookie: function() {
      this.setCookie("", "", -1); //修改2值都为空，天数为负1天就好了
    },





	},
	
}
</script>