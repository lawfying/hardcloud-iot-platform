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


		<div class="knowledge-base-jumbotron" >
			<div class="knowledge-base-jumbotron-content lg:p-12 md:p-12 sm:p-8 py-8 rounded-lg mb-base">
				<vs-row>
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
					<h1 class="mb-1 text-white">创建一个应用场景，开启行业应用之旅...</h1> 
				</vs-col>
				</vs-row>
				<vs-row>
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">	
					<vs-button @click="popupActive=true" class="mt-4" type="line" size="large" color="success">创建一个新应用场景</vs-button>
				</vs-col>
				</vs-row>				
				<vs-input placeholder="搜索应用场景名称或者关键字" v-model="knowledgeBaseSearchQuery" icon-pack="feather" icon="icon-search"  class="w-full no-icon-border mt-6" />
				<vs-row>
					
				<vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
					<div class="demo-alignment">

						<vs-popup title="创建一个新应用场景" :active.sync="popupActive" >

								<div class="vx-row">

										<div class="vx-col w-full" >
										<p> 应用场景名称<font color="#FF0000">*</font></p>
										<vs-input  v-model="scenario_title" class="w-full"/>
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 应用场景描述</p>
                                        <vs-textarea v-model="scenario_description" class="w-full" />
										</div>

										<div class="vx-col w-full" >
										<p> 上传应用场景图片<font color="#FF0000">*</font></p>
                                        <vs-input  type="file" name="file" id="imgLocal" accept="image/png,image/gif,image/jpeg"  v-model="scenario_img" class="w-full" />
										<br>
										</div>

										<div class="vx-col w-full" >
										<vs-divider/>
										<vs-button class="vx-col w-1/3 mt-3" type="border" color="success" v-on:click="addscenario">添加应用场景</vs-button>
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
						<p class="text-grey">{{ item.description.slice(0,32) }}</p>
						<vs-divider/>
						<div class="flex justify-between flex-wrap">
							<vs-button class="small"  type="border" color="primary" gradient-color-secondary="#CE9FFC" v-on:click="scenario_details(item.id)">详情</vs-button>
							<!-- <vs-button class="small" type="border" color="success"  @click="updatetemplate(item.id)">编辑</vs-button> -->
							<vs-button class="small" type="border" color="success"  @click="popupActiveSce(item)">编辑</vs-button>
							<vs-popup class="holamundo"  title="编辑模板" :active.sync="popupActiveSce_edit" background-color="rgba(0,0,0,.1)">
                                    <div class="vx-row">

										<div class="vx-col w-full" >
										<p> 应用场景名称<font color="#FF0000">*</font></p>
										<vs-input  v-model="sceTitle" class="w-full"/>
										<br>
										</div>
										<div class="vx-col w-full" >
										<p> 应用场景描述</p>
                                        <vs-textarea v-model="sceDescription" class="w-full" />
										</div>
										
										<div class="vx-col w-full" >
										<p> 更新应用场景图片</p>
                                        <input type="file" @change="triggerFile($event)" class="w-full vs-input--input">
										</div>
										<div class="vx-row" style="margin-top:50px">
											<br>
										</div>
										<div class="vx-row mb-6 w-5/6 ">
										<img :src=url+sceOld_img alt="content-img" style="margin-left:30px;"  class="responsive rounded-lg">
										</div>

										
										<vs-divider/>
										<vs-row class="vx-row w-full" style="margin-left:0px;">
										<div class="vx-col w-1/3 mt-3">
											<vs-button color="success" type="filled" @click="update_scenario(sce_id)">保存</vs-button>
										</div>
										<div class="vx-col w-1/3 mt-3">
												<vs-button color="warning" type="filled" @click="popupActiveSce_edit=false">取消</vs-button>
										</div>
										</vs-row>
										
								</div>
                                  </vs-popup>
							<!-- <vs-button class="small" type="border" color="danger" @click="deletetemplate(item.id)">删除</vs-button> -->
							<vs-button class="small" type="border" color="danger" @click="popupActiveSce2(item.id)">删除</vs-button>
						</div>
						<vs-popup class="holamundo"  title="删除模板" :active.sync="popupActiveSce_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="deletescenario(scenarioId)">确认删除</vs-button>
                                     </vs-col>

                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveSce_del=false">取消</vs-button>
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

			scenarioobject:'',
			scenarioId:'',
			scenario_title:'',
			scenario_description:'',
			device_register:'True',
			deviceprotocol:'HTTP',
			device_type:'',
			scenario_img:'',

			popupActive_del:false,

			select2_dev:'HTTP',
			options2_dev:[
				{text:'HTTP',value:'HTTP'},
				{text:'MQTT',value:'MQTT'},
			],

			popupActiveSce_edit:false,

			sceTitle:'',
			sceDescription:'',
			sce_img:'',
			sceOld_img:'',
			sce_id:'',
			imgfile:'',


			url:this.GLOBAL.baseURL,
			knowledgeBaseSearchQuery: '',
			//弹出框
			popupActive: false,
			//Form 导航
			firstName: "",
			//调用模板列表数据
			scenarios: [	
			],
			popupActiveSce_del:false,

		}
	},
	computed: {
		filteredKB() { 
			return this.scenarios.filter((item) => item.title.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()) || item.description.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()));
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

		scenario_details(param) {
			this.$router.push({ name: 'scenarioDetails', params: { scenarioId: param }})

		},

		popupActiveSce2(param) {
			this.popupActiveSce_del = true;
			this.scenarioId = param;
		},

		popupActiveSce(param) {
			this.popupActiveSce_edit = true;
			this.scenarioId = param.id;
			this.scenarioobject = param;
			this.sceTitle=param.title;
			this.sceDescription=param.description;
			this.sceOld_img=param.img;
			this.sce_id=param.id;

		},

        async addscenario()  {

			//var params= {img:this.device_img.file,title:this.template_title,description:this.template_description,
			//device_type:this.device_type,is_custom_registered:this.device_register,protocal_type:this.deviceprotocol}
			if(this.scenario_title!=''){
					let file = document.getElementById("imgLocal").files[0]
					
					let params = new FormData() // 创建form对象
					if(file) {
						params.append('img', file,file.name) // 通过append向form对象添加数据
					}
					
					let config = {
						headers: {'Content-Type': 'multipart/form-data'}
						}
					params.append('title', this.scenario_title) // 添加form表单中其他数据
					params.append('description',this.scenario_description)
					params.append('owner','1') //真实保存的是用户的，不是1

					
					const response = await this.axios.post(this.GLOBAL.baseURL+'/scenarios/',params,config).catch(function (error) {
						console.log(error)
						return error.response.data;});
						var url = this.GLOBAL.baseURL;
						var tmpimg = response.data.img;
						response.data.img=tmpimg.substring(url.length,tmpimg.length);
						this.scenarios.splice(0,0,response.data);
						this.popupActive =  false;
			}
			else{
				this.$vs.notify({
				title:'提醒：',
				text:'应用场景名称不能为空.',
				color:'danger'
			})
			}
		},

		async deletescenario(params) {
			var url = this.GLOBAL.baseURL+'/scenarios/'+params+'/';
			this.popupActiveSce_del=false;
			await this.axios.delete(url).then(function(response) {
				console.log(response);
				
			});
			
			//删除数组中的元素
          this.scenarios.forEach(function(item, index, arr) {
                if(item.id == params) {
					arr.splice(index, 1);
                }
			});
			},
		
	async update_scenario(sce_id){
		if(this.sceTitle !=''){
			let params = new FormData() // 创建form对象
			let config = {
					headers: {'Content-Type': 'multipart/form-data'}
					}
			params.append('title', this.sceTitle) // 添加form表单中其他数据
			params.append('description',this.sceDescription)

			//alert(this.imgfile[0])
			if(this.imgfile[0]) {
			params.append('img', this.imgfile[0],this.imgfile[0].name) // 通过append向form对象添加数据
			}


      

      const response = await this.axios.patch(this.GLOBAL.baseURL+'/scenarios/'+sce_id+'/',params,config).catch(function (error) {
              console.log(error)
              return error.response.data;});
       //alert(JSON.stringify(response.status))


      var url=this.url;

      this.scenarios.forEach(function(item, index, arr) {
                if(item.id == sce_id) {
                  var tmpimg = response.data.img;
                  response.data.img=tmpimg.substring(url.length,tmpimg.length);
                  arr.splice(index, 1,response.data);
                }
			});
		
		this.popupActiveSce_edit= false;
		return true;

			}
		else{
			this.$vs.notify({
				title:'提醒：',
				text:'应用场景名称不能为空.',
				color:'danger'
			})
		}
		},

		
	},
	
	mounted: async function() {


			const response = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/').catch(function (error) {
				console.log(error)
				return error.response.data;});
			console.log(response)
			if (response.status==200) {
				this.scenarios= response.data
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