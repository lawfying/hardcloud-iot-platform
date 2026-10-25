<!-- =========================================================================================
	File Name: Register.vue
	Description: Register Page
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
							<img src="@/assets/images/pages/register.jpg" alt="register" class="mx-auto">							
						</div>
						<div class="vx-col sm:w-full md:w-full lg:w-1/2 mx-auto self-center bg-white">
							<div class="p-8">
								<div class="vx-card__title">
									<h4 class="mb-4">创建账户</h4>
									<p>{{message}}</p>
								</div>
								<div class="clearfix">
									<vs-input label-placeholder="Name" placeholder="用户名" v-model="value1" class="w-full mb-6"/>
									<vs-input type="email" label-placeholder="Email" placeholder="电子邮箱" v-model="value2" class="w-full mb-6" />
									<vs-input type="password" label-placeholder="Password" placeholder="密码" v-model="value3" class="w-full mb-6" />
									<vs-input type="password" label-placeholder="Confirm Password" placeholder="重新输入密码" v-model="value4" class="w-full mb-6" />
									<vs-checkbox v-model="checkBox1" class="mb-6">我接受使用条款</vs-checkbox>
									<vs-button  type="border" to="/pages/login">登录</vs-button>
									<vs-button class="float-right" v-on:click="register">注册</vs-button>
								</div>
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
            value3: '',
            value4: '',
			checkBox1: true,
			message: '填写表单，创建新用户'
		}
	},

	methods: {

		async register ()  {

			window.sessionStorage.removeItem('Authorization');
			var params= {username:this.value1,email:this.value2,password1:this.value3,password2:this.value4}
			const response = await this.axios.post(this.GLOBAL.baseURL+'/rest-auth/registration/',params).catch(function (error) {
				console.log(error)
				return error.response.data;});
			console.log(response)
			if (response.non_field_errors) this.message = response.non_field_errors.toString();
			if (response.password1) this.message = response.password1.toString();
			if (response.username) this.message = response.username.toString();
			if (response.password2) this.message = response.password2.toString();
			var params2 =  {username:this.value1,password:this.value3}
			await this.tokenFunction(params2);
			this.$router.push('/dashboard');

			
		
		}
	},
}
</script>