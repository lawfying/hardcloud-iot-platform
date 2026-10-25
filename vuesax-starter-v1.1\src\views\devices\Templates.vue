<!-- =========================================================================================
	File Name: KnowledgeBase.vue
	Description: Knowledge Base Page
	----------------------------------------------------------------------------------------
	Item Name: Vuesax Admin - VueJS Dashboard Admin Template
	Version: 1.1
	Author: Pixinvent
	Author URL: hhttp://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>
	<div id="knowledge-base-page">
		<!-- JUMBOTRON -->


		<div class="knowledge-base-jumbotron">
			<div class="knowledge-base-jumbotron-content lg:p-12 md:p-24 sm:p-16 py-8 rounded-lg mb-base" >
				<vs-row>
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
					<h1 class="mb-1 text-white">从创建一个模板开始...</h1> 
				</vs-col>
				</vs-row>
				<vs-row>
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">	
					<vs-button @click="popupActive=true" class="mt-4" type="line" size="large" color="success">创建一个新模板</vs-button>
				</vs-col>
				</vs-row>				
				<vs-input placeholder="搜索模板名称或者关键字" v-model="knowledgeBaseSearchQuery" icon-pack="feather" icon="icon-search" class="w-full no-icon-border mt-6" />
				<vs-row>
					
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
					<div class="demo-alignment">

						<vs-popup title="创建一个新模板" :active.sync="popupActive" >

								<div class="vx-row">

										<div class="vx-col w-full" >
										<p> 模板名称<font color="#FF0000">*</font></p>
										<vs-input  v-model="template_title" class="w-full"/>
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 模板描述</p>
                                        <vs-textarea v-model="template_description" class="w-full" />
										</div>
										<!-- 20221227 -->
										<!-- <div class="vx-col w-full" >										
										<p> 设备通信协议（系统同时支持HTTP、MQTT协议）</p>
										<v-select :options="['HTTP','MQTT']" v-model="deviceprotocol" ></v-select>
										<br> 
										</div>  -->
											<div class="vx-col w-full" > 
											<p>设备型号</p>
										<vs-input  v-model="device_type" class="w-full" />
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 添加模板后上传设备模板图片</p>
                                        <vs-input  type="file" name="file" id="imgLocal" accept="image/png,image/gif,image/jpeg"  v-model="device_img" class="w-full" />
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 是否允许设备发起注册</p>
										<br>
										</div>
										<div class="vx-col w-full" >
										<ul class="centerx">
										<li>
										<vs-radio class="vx-col w-1/3 mt-3" color="success" v-model="device_register" vs-value="True">True</vs-radio>
										<vs-radio class="vx-col w-1/3 mt-3" color="danger" v-model="device_register" vs-value="False">False</vs-radio>
										</li>
										</ul>
										</div>
										<div class="vx-col w-full" >
										<vs-divider/>
										<vs-button class="vx-col w-1/3 mt-3" type="border" color="success" v-on:click="addtemplate">添加模板</vs-button>
										</div>

								</div>

						</vs-popup>
					</div>

				</vs-col>
				</vs-row>
			</div>
		</div>

		<!-- KNOWLEDGE BASE CARDS  -->
		<div class="vx-row">

				<div class="vx-col w-full sm:w-1/2 md:w-1/4  mb-base" v-for="item in filteredKB" :key="item.id">
					<vx-card> 
						<div slot="no-body">
							<img :src=url+item.img alt="content-img"  class="responsive card-img-top">
						</div>
						<h5 class="mb-2">{{ item.title }}</h5>
						<p class="text-grey" v-if="item.description.length>32">{{ item.description.slice(0,32) }}...</p>
						<p class="text-grey" v-else >{{ item.description.slice(0,32) }}</p>
						<vs-divider/>
						<div class="flex justify-between flex-wrap">
							<vs-button class="small"  type="border" color="primary" gradient-color-secondary="#CE9FFC" v-on:click="template_details(item.id)">详情</vs-button>
							<!-- <vs-button class="small" type="border" color="success"  @click="updatetemplate(item.id)">编辑</vs-button> -->
							<vs-button class="small" type="border" color="success"  @click="popupActiveTpl1(item)">编辑</vs-button>
							<vs-popup class="holamundo"  title="编辑模板" :active.sync="popupActiveTpl_edit" background-color="rgba(0,0,0,.1)">
                                    <div class="vx-row">

										<div class="vx-col w-full" >
										<p> 模板名称<font color="#FF0000">*</font></p>
										<vs-input  v-model="tplTitle" class="w-full"/>
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 模板描述</p>
                                        <vs-textarea v-model="tplDescription" class="w-full" />
										</div>
										<div class="vx-col w-full" >										
										<p> 设备通信协议</p>
										<v-select :options="['HTTP','MQTT']" v-model="tplProtocal_type" ></v-select>
										<br> 
										</div> 
											<div class="vx-col w-full" > 
											<p>设备型号</p>
										<vs-input  v-model="tplDevice_type" class="w-full" />
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 更新模板图片</p>
                                        <input type="file" @change="triggerFile($event)" class="w-full vs-input--input">
										</div>
										<div class="vx-row" style="margin-top:50px">
											<br>
										</div>
										<div class="vx-row mb-6 w-5/6 ">
										<img :src=url+tplOld_img alt="content-img" style="margin-left:30px;"  class="responsive rounded-lg">
										</div>
										<div class="vx-col w-full" >
										<p> 是否允许设备发起注册</p>
										<br>
										</div>
										<div class="vx-col w-full" >
										<ul class="centerx">
										<li>
										<vs-radio class="vx-col w-1/3 mt-3" color="success" v-model="tpl_register" vs-value="true">True</vs-radio>
										<vs-radio class="vx-col w-1/3 mt-3" color="danger" v-model="tpl_register" vs-value="false">False</vs-radio>
										</li>
										</ul>
										</div>
										<vs-divider/>
										<vs-row class="vx-row w-full" style="margin-left:0px;">
										<div class="vx-col w-1/3 mt-3">
											<vs-button color="success" type="filled" @click="update_template(tpl_id)">保存</vs-button>
										</div>
										<div class="vx-col w-1/3 mt-3">
												<vs-button color="warning" type="filled" @click="popupActiveTpl_edit=false">取消</vs-button>
										</div>
										</vs-row>
										
								</div>
                                  </vs-popup>
							<!-- <vs-button class="small" type="border" color="danger" @click="deletetemplate(item.id)">删除</vs-button> -->
							<vs-button class="small" type="border" color="danger" @click="popupActiveTpl2(item.id)">删除</vs-button>
						</div>
						<vs-popup class="holamundo"  title="删除模板" :active.sync="popupActiveTpl_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="deletetemplate(templateId)">确认删除</vs-button>
                                     </vs-col>

                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveTpl_del=false">取消</vs-button>
                                    </vs-col>
                                    </vs-row>
                                  </vs-popup>
					</vx-card>
				</div>

		</div>	
	</div>
</template>

<script>
import {FormWizard, TabContent} from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import vSelect from 'vue-select'


export default{
	data() {
		return {
			users: [
				{
				"id": 1,
				"name": "Leanne Graham",
				"username": "Bret",
				"email": "Sincere@april.biz",
				"website": "hildegard.org",
				},
				{
				"id": 2,
				"name": "Ervin Howell",
				"username": "Antonette",
				"email": "Shanna@melissa.tv",
				"website": "anastasia.net",
				},
			],
			templateobject:'',
			templateId:'',
			template_title:'',
			template_description:'',
			device_register:'True',
			deviceprotocol:'HTTP',
			device_type:'',
			device_img:'',

			popupActive_del:false,

			select2_dev:'HTTP',
			options2_dev:[
				{text:'HTTP',value:'HTTP'},
				{text:'MQTT',value:'MQTT'},
			],

			tplTitle:'',
			tplDescription:'',
			tplProtocal_type:'',
			tplDevice_type:'',
			tpl_img:'',
			tplOld_img:'',
			tpl_register:'',
			tpl_id:'',
			imgfile:'',



			category: [
				{
				categoryId: "INR",
				categoryName: "India",
				},
				{
				categoryId: "INRdd",
				categoryName: "Indiadd",
				},

			],
			url:this.GLOBAL.baseURL,
			knowledgeBaseSearchQuery: '',
			//弹出框
			popupActive: false,
			//Form 导航
			firstName: "",
			//调用模板列表数据
			kb: [	
			],
			popupActiveTpl_del:false,
			popupActiveTpl_edit:false,
		}
	},
	computed: {
		filteredKB() { 
			return this.kb.filter((item) => item.title.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()) || item.description.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()));
		}
	},
	methods: {

		triggerFile : function (event) {
		this.imgfile = event.target.files; // (利用console.log输出看结构就知道如何处理档案资料)
		// do something...
		},
		formSubmitted() {
			alert("Form submitted!");
		},

		template_details(param) {
			this.$router.push({ name: 'templateDetails', params: { templateId: param }})

		},

		popupActiveTpl2(param) {
			this.popupActiveTpl_del = true;
			this.templateId = param;
		},

		popupActiveTpl1(param) {
			this.popupActiveTpl_edit = true;
			this.templateId = param.id;
			this.templateobject = param;
			this.tplTitle=param.title;
			this.tplDescription=param.description;
			this.tplProtocal_type=param.protocal_type;
			this.tplDevice_type=param.device_type;
			this.tplOld_img=param.img;
			this.tpl_id=param.id;
			if(param.is_custom_registered){
			this.tpl_register="true";
			}
			else{
			this.tpl_register="false";
         }

		},

        async addtemplate ()  {

			//var params= {img:this.device_img.file,title:this.template_title,description:this.template_description,
			//device_type:this.device_type,is_custom_registered:this.device_register,protocal_type:this.deviceprotocol}
			if(this.template_title!='') {
				let file = document.getElementById("imgLocal").files[0]
			
				let params = new FormData() // 创建form对象
				if(file) {
					params.append('img', file,file.name) // 通过append向form对象添加数据
				}
				
				let config = {
					headers: {'Content-Type': 'multipart/form-data'}
					}
				params.append('title', this.template_title) // 添加form表单中其他数据
				params.append('description',this.template_description)
				params.append('device_type',this.device_type)
				params.append('is_custom_registered',this.device_register)
				params.append('protocal_type',this.deviceprotocol)
				
				const response = await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/',params,config).catch(function (error) {
					console.log(error)
					return error.response.data;});
					var url = this.GLOBAL.baseURL;
					var tmpimg = response.data.img;
					response.data.img=tmpimg.substring(url.length,tmpimg.length);
					this.kb.splice(0,0,response.data);
					this.popupActive =  false;
					this.template_title = '';
					this.template_description = '';
					this.device_type = '';
			}
			else{
				this.$vs.notify({
				title:'提醒：',
				text:'设备模板名称不能为空.',
				color:'danger'
			})
			}
			
		},

		async deletetemplate(params) {
			var url = this.GLOBAL.baseURL+'/devtemplates/'+params+'/';
			this.popupActiveTpl_del=false;
			await this.axios.delete(url).then(function(response) {
				console.log(response);
				
			});
			
			//删除数组中的元素
          this.kb.forEach(function(item, index, arr) {
                if(item.id == params) {
					arr.splice(index, 1);
                }
			});
			},
		
	async update_template(tpl_id){
		if(this.tplTitle!=''){
			let params = new FormData() // 创建form对象
			let config = {
					headers: {'Content-Type': 'multipart/form-data'}
					}
			params.append('title', this.tplTitle) // 添加form表单中其他数据
			params.append('description',this.tplDescription)
			params.append('device_type',this.tplDevice_type)
			params.append('is_custom_registered',this.tpl_register)
			params.append('protocal_type',this.tplProtocal_type)
			//alert(this.imgfile[0])
			if(this.imgfile[0]) {
			params.append('img', this.imgfile[0],this.imgfile[0].name) // 通过append向form对象添加数据
		}


		

		const response = await this.axios.patch(this.GLOBAL.baseURL+'/devtemplates/'+tpl_id+'/',params,config).catch(function (error) {
				console.log(error)
				return error.response.data;});
		//alert(JSON.stringify(response.status))


		var url=this.url;

		this.kb.forEach(function(item, index, arr) {
					if(item.id == tpl_id) {
					var tmpimg = response.data.img;
					response.data.img=tmpimg.substring(url.length,tmpimg.length);
					arr.splice(index, 1,response.data);
					}
				});
			
			this.popupActiveTpl_edit= false;
			return true;
		}
		else{
				this.$vs.notify({
				title:'提醒：',
				text:'设备模板名称不能为空.',
				color:'danger'
			})
			}
		
		},
		
	},
	
	mounted: async function() {


			const response = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/').catch(function (error) {
				console.log(error)
				return error.response.data;});
			console.log(response)
			if (response.status==200) {
				this.kb = response.data
			} 

	},

	components: {
		'v-select': vSelect,
		FormWizard,
		TabContent
	}
}
</script>

<style lang="scss">
.knowledge-base-jumbotron-content {
	background-image: url('../../assets/images/pages/knowledge-base-cover.jpg');
	background-size: cover;
}
</style>