<template>
  <div class="mt-5">

    <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <vs-select autocomplete placeholder="选择设备模板" class="selectExample" v-model="select1" :danger="select_danger" :input-changed="select_changed()">
        <vs-select-item :key="index" :value="item.id" :text="item.title" v-for="(item,index) in options1" />
        </vs-select>
        </vs-col>

        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
        <div class="centerx" > 
        <span> 选择数量</span>
        </div>
        </vs-col>

        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
        <div class="centerx"> 
        <vs-input-number v-model="number0" :min="1" :max="5" :step="1"/>
        </div>
        </vs-col>

        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <div class="centerx"> 
        <vs-button color="success" size="small" type="filled" @click="createDevices()">生成设备</vs-button>
        </div>
        </vs-col>

         <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
      <div class="centerx"> 

    </div>
    </vs-col>

    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="5">
        <vs-input placeholder="搜索设备名称、设备描述或者TokenID号" v-model="knowledgeBaseSearchQuery"  icon-pack="feather" icon="icon-search"  class="w-full no-icon-border mt-4" />
    </vs-col>

    </vs-row>

        <vs-divider/>

    




  <vs-table pagination max-items="10" :data="filteredKB" stripe>

    <template slot="thead">
      <!-- <vs-th>序号</vs-th> -->
      <vs-th>设备图标</vs-th>
      <vs-th>设备名称</vs-th>
      <vs-th>设备TokenID</vs-th>
      <vs-th>设备状态</vs-th>
      <vs-th>创建时间</vs-th>
      <vs-th style="padding-left:50px;">操作</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
        
        <!-- <vs-td :data="data[indextr].id">
          {{ indextr+1 }}
        </vs-td> -->

        <vs-td :data="data[indextr].img">
          <img :src=url+data[indextr].img  alt="" width="30" height="30" class="rounded shadow-md cursor-pointer block">
        </vs-td>

        <vs-td :data="data[indextr].title">
        {{ data[indextr].title }}
        </vs-td>

        <vs-td :data="data[indextr].id">
         <span  @click="device_details(tr.id)" class="text-success"><u> {{ data[indextr].id }} </u></span>
        </vs-td>


        <vs-td :data="data[indextr].status">
          {{ data[indextr].status }}
        </vs-td>

        <vs-td :data="data[indextr].created">
          {{ data[indextr].created | formatDate }}
        </vs-td>

        <vs-td>
          <!-- <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger"> 
                <vx-tooltip color="success" text="详情">
                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-file-text" @click="device_details(tr.id)"> </vs-button>
                </vx-tooltip>
             </span>                    
        </vs-col> -->
        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger"> 
                <vx-tooltip color="success" text="编辑">
                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveDev1(tr)"> </vs-button>
                
                </vx-tooltip>
             </span>                    
        </vs-col>

         <vs-popup title="编辑设备" :active.sync="popupActiveDev_edit" background-color="rgba(0,0,0,.1)">

                    <div class="vx-col w-full mb-base">
                          <vx-card>
                            <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                                <vs-input class="w-full" label="设备名称" v-model="deviceTitle" />
                              </div>
                            </div>
                            <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                                <span class="vs-input--label">设备描述</span>
                                <vs-textarea class="w-full" v-model="deviceDecription" />
                              </div>
                            </div>
                            <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                                <vs-input class="w-full" label="设备型号" v-model="deviceType" />
                              </div>
                            </div>
                            <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                                <vs-input class="w-full" label="注册码" v-model="registerCode" />
                              </div>
                            </div>
                            <!-- <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                             <span class="vs-input--label">设备通讯协议</span>
                                <v-select label="deviceProtocol" :options="['HTTP','MQTT']" v-model="deviceprotocal"></v-select>
       
                              </div>
                            </div> -->

                            <div class="vx-row mb-6">
                              <div class="vx-col w-full">
                             <span class="vs-input--label">设备状态</span>
                                <v-select label="deviceStatus" :options="['UNACTIVE','ACTIVE','ONLINE','OFFLINE']" v-model="devicestatus"></v-select>
       
                              </div>
                            </div>

                            <div class="vx-col w-full" >
                            <p class="vs-input--label"> 是否允许设备发起注册</p>
                            </div>
                            <div class="vx-col w-full" >
                            <ul class="centerx">
                            <li>
                            <vs-radio class="vx-col w-1/3 mt-3" color="success" v-model="device_register" vs-value="true">True</vs-radio>
                            <vs-radio class="vx-col w-1/3 mt-3" color="danger" v-model="device_register" vs-value="false">False</vs-radio>
                            </li>
                            </ul>
                            </div>
                            <br>

                            <div class="vx-col w-full" >
                            <p class="vs-input--label"> 更新设备图片</p>
                            <input type="file" @change="triggerFile($event)" class="w-full vs-input--input">
                            </div>
                             <div class="vx-row" style="margin-top:20px">
                            </div>

                            <div class="vx-row mb-6 w-5/6 ">
                              <img :src=url+device_img_old alt="content-img" style="margin-left:10px;"  class="responsive rounded-lg">
                            </div>

                            <vs-divider/>

                            <div class="vx-row mb-6">
                              <div class="vx-col sm:w-1/3 w-full">
                                <vs-button color="success" type="filled" @click="update_device(dev_id)">保存</vs-button>
                              </div>
                              <div class="vx-col sm:w-2/3 w-full">
                                <vs-button color="warning" type="filled" @click="popupActiveDev_edit=false">取消</vs-button>
                              </div>
                            </div>
                          </vx-card>
                        </div>
                               
                 </vs-popup>



        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger"> 
                <vx-tooltip color="danger" text="删除">
                <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveTag2(tr.id,indextr)"> </vs-button>

                                   <vs-popup class="holamundo"  title="删除设备" :active.sync="popupActiveDev_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="delete_device(dev_id)">确认删除</vs-button>
                                     </vs-col>

                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveDev_del=false">取消</vs-button>
                                    </vs-col>
                                    </vs-row>
                                  </vs-popup>
                </vx-tooltip>
             </span>                    
        </vs-col>
        </vs-td>


      </vs-tr>
    </template>
  </vs-table>
  </div>

</template>

<script>


var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}

import {FormWizard, TabContent} from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import vSelect from 'vue-select'

export default {


  data() {
    return {
      popupActiveDev_del:false,
      popupActiveDev_edit:false,
      dev_id:'',
      dev_index:'',

      select1:0,
      options1:[],
      number0:1,
      select_danger:false,

      devices:[],
      url:this.GLOBAL.baseURL,
      knowledgeBaseSearchQuery: '',

      deviceprotocal:'',
      devicestatus:'',
      device_register:'',
      device_img:'',
      deviceTitle:'',
      deviceDecription:'',
      deviceType:'',
      registerCode:'',
      device_img_old:'',

      imgfile:'',
      tooltipact:true,

      
    }
  },
  computed: {
		filteredKB() { 
			return this.devices.filter((item) => item.title.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()) || item.id.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()));
    }
    
    },
    
        filters:{
        formatDate:function (val) {
            var value=new Date(val);
            var year=value.getFullYear();
            var month=padDate(value.getMonth()+1);
            var day=padDate(value.getDate());
            var hour=padDate(value.getHours());
            var minutes=padDate(value.getMinutes());
            var seconds=padDate(value.getSeconds());
            return year+'-'+month+'-'+day+' '+hour+':'+minutes+':'+seconds;
 
        }
    },

  created: async function() {

      const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/').catch(function (error) {
			console.log(error)
            return error.response.data;});
      if (response.status==200) {
          this.devices = response.data;
      }

      const response1 = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/').catch(function (error) {
			console.log(error)
            return error.response1.data;});
      if (response1.status==200) {
          this.options1 = response1.data;
      }
  },

  methods:{

    triggerFile : function (event) {
  this.imgfile = event.target.files; // (利用console.log输出看结构就知道如何处理档案资料)
  // do something...
},



      async createDevices() {
         var devnum = this.number0;
         var tplid = this.select1;
         var params ={"devtemplate":tplid}

         if (this.select1=='') {
             this.select_danger=true;

             return true;
         }

         for(var i=0;i<devnum;i++){
            const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/createDevByTpl/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
            if(response.status=='200'){
                this.devices.unshift(response.data);

            }
         }

       },

    select_changed(){
        if (this.select1!='') {
            this.select_danger = false;
        }
        
        return true;
    },

    popupActiveTag2(param1,param2){
         this.popupActiveDev_del=true;
         this.dev_id = param1;
         this.dev_index = param2;

       },

    popupActiveDev1(param1){
         this.popupActiveDev_edit=true;
         var tmp = param1;
         this.dev_id = tmp.id;
         this.deviceTitle=tmp.title;
         this.deviceDecription=tmp.description;
         this.deviceType=tmp.device_type;
         this.registerCode=tmp.register_code;
         this.deviceprotocal=tmp.protocal_type;
         this.devicestatus=tmp.status;
         if(tmp.is_custom_registered){
           this.device_register="true";
         }
         else{
           this.device_register="false";

         }

         this.device_img_old=tmp.img;


       },


    async update_device(dev_id){
      
     // let file = document.getElementById("imgLocal1").files[0]
      if(this.deviceTitle!=''){
          let params = new FormData() // 创建form对象
          
          let config = {
            headers: {'Content-Type': 'multipart/form-data'}
            }
          params.append('title', this.deviceTitle) // 添加form表单中其他数据
          params.append('description',this.deviceDecription)
          params.append('device_type',this.deviceType)
          params.append('is_custom_registered',this.device_register)
          params.append('protocal_type',this.deviceprotocal)
          params.append('status',this.devicestatus)
          params.append('register_code',this.registerCode)

          //alert(this.imgfile[0])

          if(this.imgfile[0]) {
            params.append('img', this.imgfile[0],this.imgfile[0].name) // 通过append向form对象添加数据
          }

          

          const response = await this.axios.patch(this.GLOBAL.baseURL+'/devices/'+dev_id+'/',params,config).catch(function (error) {
                  console.log(error)
                  return error.response.data;});

          var url=this.url;

          this.devices.forEach(function(item, index, arr) {
                    if(item.id == dev_id) {
                      var tmpimg = response.data.img;
                      response.data.img=tmpimg.substring(url.length,tmpimg.length);
                      arr.splice(index, 1,response.data);
                    }
                });
          this.popupActiveDev_edit= false;
          
          
          return true;
      }
      else{
        this.$vs.notify({
            title:'提醒：',
            text:'设备名称不能为空.',
            color:'danger'
          })
      }

       },





    async delete_device(dev_id){

        var devid = dev_id;
        
         var url = this.GLOBAL.baseURL+'/devices/'+devid+'/';
         this.popupActiveDev_del=false;
         await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          //删除数组中的元素

          //删除数组中的元素
          this.devices.forEach(function(item, index, arr) {
                if(item.id == devid) {
                    arr.splice(index, 1);
                }
            });
 
         return true;
    },

    device_details(param) {
      this.$router.push({ name: 'deviceDetails', params: { deviceId: param }});

    },
  },

  
	components: {
		'v-select': vSelect,
		FormWizard,
		TabContent
	}
  


}
</script>