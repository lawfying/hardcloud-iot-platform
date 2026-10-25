<template>
  <div class="mt-5">

    <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">
        <vs-select autocomplete placeholder="选择设备" v-model="select1" :danger="select_danger" :input-changed="select_changed()" width="600px">
        <vs-select-item :key="index" :value="item.id" :text="'设备名称:'+item.title+'----ID:'+item.id" v-for="(item,index) in options1" />
        </vs-select>
        </vs-col>


        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
        <div class="centerx"> 
        <vs-button color="success" size="small" type="filled" @click="createSubDevices()">添加订阅设备</vs-button>
        </div>
        </vs-col>

         <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
      <div class="centerx"> 

    </div>
    </vs-col>

    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="5">
        <vs-input placeholder="搜索订阅设备或订阅主题" v-model="knowledgeBaseSearchQuery"  icon-pack="feather" icon="icon-search"  class="w-full no-icon-border mt-4" />
    </vs-col>

    </vs-row>

        <vs-divider/>

    




  <vs-table pagination max-items="10" :data="filteredKB" stripe>

    <template slot="thead">
      <!-- <vs-th>序号</vs-th> -->
      <vs-th>订阅设备</vs-th>
      <vs-th>订阅主题</vs-th>
      <vs-th>订阅状态</vs-th>
      <vs-th>状态说明</vs-th>
      <vs-th style="padding-left:60px;">操作</vs-th>
    </template>

    <template slot-scope="{data}">
      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
        
        <!-- <vs-td :data="data[indextr].id">
          {{ indextr+1 }}
        </vs-td> -->


        <vs-td :data="data[indextr].device_title">
        {{ data[indextr].device_title }}
        </vs-td>

        <vs-td :data="data[indextr].topic">
         {{ data[indextr].topic }}
        </vs-td>


        <vs-td :data="data[indextr].status">
          {{ data[indextr].status }}
        </vs-td>

        <vs-td :data="data[indextr].status">
          <span class="text-success" v-if = "data[indextr].status=='SUBSCRIBED'">MQTT已订阅</span> <span class="text-warning" v-else>MQTT未订阅</span>
        </vs-td>

        <vs-td>
          <!-- <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger"> 
                <vx-tooltip color="success" text="详情">
                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-file-text" @click="device_details(tr.id)"> </vs-button>
                </vx-tooltip>
             </span>                    
        </vs-col> -->
        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-if="tr.status=='UNSUBSCRIBED'">
              <span class="text-danger"> 
                <vx-tooltip color="success" text="启动订阅">
                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-play" @click="subscribe_start(tr,indextr)"> </vs-button>
                
                </vx-tooltip>
             </span>                    
        </vs-col>
        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-else>
              <span class="text-danger"> 
                <vx-tooltip color="warning" text="暂停订阅">
                <vs-button radius color="warning" type="flat" icon-pack="feather" icon="icon-pause" @click="subscribe_stop(tr,indextr)"> </vs-button>
                
                </vx-tooltip>
             </span>                    
        </vs-col>

        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger"> 
                <vx-tooltip color="danger" text="删除">
                <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveTag2(tr.id,indextr)"> </vs-button>

                                   <vs-popup class="holamundo"  title="删除设备" :active.sync="popupActiveDev_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="delete_subdevice(subdev_id)">确认删除</vs-button>
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


import {FormWizard, TabContent} from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import vSelect from 'vue-select'

export default {


  data() {
    return {
      popupActiveDev_del:false,
      popupActiveDev_edit:false,
      subdev_id:'',
      subdev_index:'',

      select1:0,
      options1:[],
      number0:1,
      select_danger:false,

      subdevices:[],
      url:this.GLOBAL.baseURL,
      knowledgeBaseSearchQuery: '',

      
    }
  },
  computed: {
		filteredKB() { 
			return this.subdevices.filter((item) => item.device_title.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()) || item.topic.toLowerCase().includes(this.knowledgeBaseSearchQuery.toLowerCase()));
    }
    
    },
    

  created: async function() {

      const response = await this.axios.get(this.GLOBAL.baseURL+'/iotsubdev/devices/').catch(function (error) {
			console.log(error)
            return error.response.data;});
      if (response.status==200) {
          this.subdevices = response.data;
      }

      const response1 = await this.axios.get(this.GLOBAL.baseURL+'/devices/').catch(function (error) {
			console.log(error)
            return error.response1.data;});

      response1.data.forEach(function(item,index,arr) {
          for(var tmp in response.data) {
              if  (response.data[tmp].topic == item.id){
                  arr.splice(index,1)
              }
          } 
      });

      this.options1 = response1.data;

  },

  methods:{

      async createSubDevices() {
         var devid = this.select1;
         var params ={}

         if (this.select1=='') {
             this.select_danger=true;
             return true;
         }

         const response = await this.axios.post(this.GLOBAL.baseURL+'/iotsubdev/devices/'+devid+'/iotsubdevs/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
        if(response.status=='200'){
                this.subdevices.unshift(response.data);
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
         this.subdev_id = param1;
         this.subdev_index = param2;

       },

    async subscribe_start(tr,indextr){

        var params={'status':'SUBSCRIBE'}

        const response = await this.axios.post(this.GLOBAL.baseURL+'/iotsubdev/devices/'+tr.device+'/iotsubdevs/subscribe/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
        if(response.status=='200'){
                this.subdevices[indextr].status='SUBSCRIBED';
            }

    },

    async subscribe_stop(tr,indextr){

        var params={'status':'UNSUBSCRIBE'}

        const response = await this.axios.post(this.GLOBAL.baseURL+'/iotsubdev/devices/'+tr.device+'/iotsubdevs/subscribe/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
        if(response.status=='200'){
                this.subdevices[indextr].status='UNSUBSCRIBED';
            }

    },

    
    async delete_subdevice(subdev_id){

        var subdevid = subdev_id;
        
         var url = this.GLOBAL.baseURL+'/iotsubdev/devices/'+subdevid+'/';
         this.popupActiveDev_del=false;
         await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          //删除数组中的元素

          //删除数组中的元素
          this.subdevices.forEach(function(item, index, arr) {
                if(item.id == subdevid) {
                    arr.splice(index, 1);
                }
            });
 
         return true;
    },


  },

  
	components: {
		'v-select': vSelect,
		FormWizard,
		TabContent
	}
  


}
</script>