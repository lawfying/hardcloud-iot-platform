<!-- =========================================================================================
	File Name: PopupInnerPopup.vue
	Description: create inner popup
	----------------------------------------------------------------------------------------
	Item Name: Vuesax Admin - VueJS Dashboard Admin Template
	Version: 1.1
	Author: Pixinvent
	Author URL: hhttp://www.themeforest.net/user/pixinvent
========================================================================================== -->


<template>

          <div class="flex flex-wrap">

          <vs-tabs vs-alignment="fixed" >
           <vs-tab vs-label="关联设备">

            <vs-row>
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
 
             <vx-card class="overlay-card overflow-hidden">
                 <vs-col  class="w-1/3">
                    <p class="w-full">设备组合名称： <span class="text-success" >{{ devcollection.title }} </span></p>
                 </vs-col>
                 <vs-col class="w-1/3">
                      设备组合ID：<span class="text-success" > {{ devcollection.id }}  </span>
                 </vs-col>
                 <vs-col class="w-1/3">
                      所属应用场景名称： <span class="text-success" > {{ scenarioName }} </span>
                 </vs-col>
                 <vs-col>
                   <br>
                    <!-- <p class="w-full">设备组合描述： {{ devcollection.description }}</p> -->
                  </vs-col>
            <vs-divider/>

             <vs-row>

                  
                <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
                <vs-select autocomplete placeholder="选择设备" v-model="select1" :danger="select_danger" :input-changed="select_changed()" width="600px">
                <vs-select-item :key="index" :value="item.id" :text="'设备名称:'+item.title+'----ID:'+item.id" v-for="(item,index) in options1" />
                </vs-select>
                </vs-col>

                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                    <vs-button color="success" type="border" icon-pack="feather" icon="icon-plus"  v-on:click="adddevlink()">添加设备关联</vs-button>
                  </vs-col>
             </vs-row>

           <vs-divider/>
              <vs-table max-items="5" pagination :data="devlinks">

                <template slot="thead">
                  <vs-th>设备名称</vs-th>
                  <vs-th>设备ID</vs-th>
                  <vs-th>关联ID</vs-th>
                  <vs-th>链接至该设备</vs-th>
                  <vs-th>移除设备组合</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td :data="data[indextag].device_title">
                      {{ data[indextag].device_title }}
                    </vs-td>

                    <vs-td :data="data[indextag].device_id">
                    {{ data[indextag].device_id }}
                    </vs-td>
                    <vs-td :data="data[indextag].device_id">
                    {{ data[indextag].devlink_id }}
                    </vs-td>
                     <vs-td>

                            <vs-row>
                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-success"> 
                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-arrow-right" @click="device_details(tag.device_id)"></vs-button>
                              </span>
                              
                            </vs-col>

                            </vs-row>
                    </vs-td>
                    <vs-td>
                    <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-shield-off" @click="popupActiveDev(tag)"> </vs-button>
                                  <vs-popup class="holamundo"  title="移除设备" :active.sync="popupActiveDev_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="danger" type="filled" @click="deldevlink(devlinkid)">确认移除</vs-button>
                                     </vs-col>
                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveDev_del=false">取消</vs-button>
                                    </vs-col>
                                    </vs-row>
                                  </vs-popup>
                    </vs-td>

                  </vs-tr>
                </template>
              </vs-table>



            </vx-card>
    

              </vs-col>
              </vs-row>

                  </vs-tab>

            <vs-tab vs-label="一键设置" @click="initsettings()">
              <vs-row>
              <div class="w-full sm:w-1/2 md:w-2/4 px-2">
                <vx-card class="overlay-card overflow-hidden">
                 <vs-row>
                  <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="4">
                    <vs-input class="inputx w-full" placeholder="名称" v-model="settingTitle" />
                  </vs-col>
                  <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="8">
                    <vs-input class="inputx w-full" placeholder="设备组合设置描述" v-model="settingDescript" />
                  </vs-col>
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12"><br></vs-col>
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                    <vs-button color="success" type="border" icon-pack="feather" icon="icon-plus"  v-on:click="addsetting()">添加设备组合设置</vs-button>
                  </vs-col>
                  </vs-row>
                   <vs-divider/>
                  <br>
                 <vs-table max-items="10" pagination :data="settingList">

                <template slot="thead">
                  <vs-th>ID号</vs-th>
                  <vs-th>名称</vs-th>
                  <vs-th>描述</vs-th>
                  <div style="padding-left:100px;">
                  <vs-th>操作</vs-th>
                  </div>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td :data="data[indextag].id">
                      {{ data[indextag].id }}
                    </vs-td>

                    <vs-td :data="data[indextag].title">
                      {{ data[indextag].title }}
                    </vs-td>

                    <vs-td :data="data[indextag].description">
                      {{ data[indextag].description.slice(0,20) }}
                    </vs-td>
                    <vs-td>
                            <vs-row>
                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="关联通道"> 
                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-file-text" v-on:click="show_ctrlchannel(tag)"></vs-button>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>

                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveSet_updatefunc(tag)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑设备组合设置" :active.sync="popupActiveSet_update" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     设备组合设置名称：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="settitle_input"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     设备组合设置描述：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-textarea class="inputx" v-model="setdescript_input"/>
                                    </vs-col> 
                                    <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="ctrlsetting_update(tmp_setting)">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-danger"> 
                                <vx-tooltip color="danger" text="删除">
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveSet(tag)"> </vs-button>
                                  <vs-popup class="holamundo"  title="删除组合设置" :active.sync="popupActiveSet_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="danger" type="filled" @click="delctrlset(tmp_setting)">确认删除</vs-button>
                                     </vs-col>
                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveSet_del=false">取消</vs-button>
                                    </vs-col>
                                    </vs-row>
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                            </vs-col>

                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-success"> 
                                <vx-tooltip color="success" text="一键控制">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-settings" @click="oneButtonControl(tag)"> </vs-button>
                                </vx-tooltip>
                              </span>
                            </vs-col>

                            </vs-row>
                    </vs-td>

                  </vs-tr>
                </template>
              </vs-table>
                </vx-card>
              </div>
              <div class="w-full sm:w-1/2 md:w-2/4 px-2" v-show="showctrlchannel">
                <vx-card class="overlay-card overflow-hidden">
                  <h6>设备组合设置名称：{{ showsettingtitle }}</h6>
                  <p> 设备组合设置描述：{{ showsettingdescription }}</p>
                  <vs-divider>控制通道</vs-divider>

                   <vs-table max-items="5" pagination :data="selected_linkchannels">

                    <template slot="thead">
                      <vs-th>设备名称</vs-th>
                      <vs-th>通道名称</vs-th>
                      <vs-th>通道ID</vs-th>
                      <vs-th>添加参数</vs-th>
                      <vs-th>参数</vs-th>
                      <vs-th>操作</vs-th>
                    </template>

                    <template slot-scope="{data}">
                      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

                        <vs-td :data="data[indextr].device_title">
                          {{ data[indextr].device_title }}
                        </vs-td>

                        <vs-td :data="data[indextr].channel_title">
                          {{ data[indextr].channel_title }}
                        </vs-td>
                        <vs-td :data="data[indextr].channel_id">
                          {{ data[indextr].channel_id }}
                        </vs-td>

                        <vs-td>
                          <vs-button color="success" type="flat" icon-pack="feather" icon="icon-plus"  v-on:click="popupActiveSet_addparam(tr)"></vs-button>
                                  <vs-popup class="holamundo"  title="添加参数" :active.sync="popupActiveSet_addsetparam" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                    注意：与通道数据类型要求要一致
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     KEY：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="setparamkey_input"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     VALUE：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="setparamvalue_input"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <br>
                                    </vs-col> 
                                   <vs-divider/>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="ctrlsetting_addparam(linkchn_tmpid)">添加</vs-button>
                                      <vs-button color="warning" type="filled" @click="popupActiveSet_addsetparam=false">关闭</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                        </vs-td>

                        <vs-td>
                         <vs-button color="success" type="flat" icon-pack="feather"  v-on:click="popupActiveSet_viewparam(tr)">查看参数</vs-button>
                                  <vs-popup class="holamundo"  title="查看参数" :active.sync="popupActiveSet_viewsetparam" background-color="rgba(0,0,0,.1)">
                                    <vs-table max-items="5" pagination :data="paramList">

                                    <template slot="thead">
                                      <vs-th>ID</vs-th>
                                      <vs-th>KEY</vs-th>
                                      <vs-th>VALUE</vs-th>
                                    </template>

                                    <template slot-scope="{data}">
                                      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

                                        <vs-td :data="data[indextr].id">
                                          {{ data[indextr].id }}
                                        </vs-td>

                                        <vs-td :data="data[indextr].key">
                                          {{ data[indextr].key }}
                                        </vs-td>

                                        <vs-td :data="data[indextr].value">
                                          {{ data[indextr].value }}
                                        </vs-td>

                                      </vs-tr>
                                    </template>
                                  </vs-table>
                                   
                                  </vs-popup>
                        </vs-td>

                        <vs-td>
                        <vs-row>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-danger"> 
                                <vx-tooltip color="danger" text="删除">
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveLinkCtrl(tr)"> </vs-button>
                                  <vs-popup class="holamundo"  title="删除关联控制通道" :active.sync="popupActiveLinkCtrl_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="danger" type="filled" @click="dellinkctrl(tmp_linkctrl)">确认删除</vs-button>
                                     </vs-col>
                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveLinkCtrl_del=false">取消</vs-button>
                                    </vs-col>
                                    </vs-row>
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                            </vs-col>
                            </vs-row>
                    </vs-td>

                      </vs-tr>
                    </template>
                  </vs-table>
                  
                   <vs-collapse accordion>

                    <vs-collapse-item>
                      <div slot="header">
                       <h6> 选择控制通道 </h6>
                      </div>
                      <vs-button color="success" type="flat" icon-pack="feather" icon="icon-plus"  v-on:click="addlinkctrlchannel()">添加关联设备通道</vs-button>
                      <vs-table multiple v-model="selected" @selected="handleSelected" :data="linkchannels">

                                    <template slot="thead">
                                      <vs-th>通道名称</vs-th>
                                      <vs-th>通道类型</vs-th>
                                      <vs-th>所属设备</vs-th>
                                    </template>

                                    <template slot-scope="{data}">
                                      <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">

                                        <vs-td :data="data[indextr].title">
                                          {{ data[indextr].title }}
                                        </vs-td>

                                        <vs-td :data="data[indextr].datatype">
                                          {{ data[indextr].datatype }}
                                        </vs-td>

                                        <vs-td :data="data[indextr].device_title">
                                          {{ data[indextr].device_title }}
                                        </vs-td>

                                      </vs-tr>
                                    </template>
                                  </vs-table>
                                  
                    </vs-collapse-item>
                  </vs-collapse>
                </vx-card>
              </div>
              </vs-row>
            </vs-tab>

 

    </vs-tabs>

        </div>

</template>

<script>

export default {
	data() {
		return {
            url:'',
            scenarioName:'',
            scenarioDescription:'',
            createdDate:'',
            updatedDate:'',

            scenarioId:'',
            collectionId:'',
            devcollection:[],
            devlinks:[],

            select1:0,
            options1:[],
            number0:1,
            select_danger:false,
            popupActiveDev_del:false,
            devlinkid:'',

            settingTitle:'',
            settingDescript:'',
            settingList:[],

            showctrlchannel:false,
            showsettingtitle:'',
            showsettingdescription:'',
            showsettingid:'',
            linkchannels:[],

            selected: [],
            selected_linkchannels:[],

            popupActiveSet_del:false,
            tmp_setting:'',
            popupActiveSet_update:false,
            settitle_input:'',
            setdescript_input:'',

            popupActiveSet_addsetparam:false,
            linkchn_tmpid:'',
            setparamkey_input:'',
            setparamvalue_input:'',

            popupActiveSet_viewsetparam:false,
            paramList:[],
            popupActiveLinkCtrl_del:false,
            tmp_linkctrl:[],
            selected_linkchannels_ctrl:[]


		}
    },
     mounted: async function() {
      var tmp;
      if (!this.$route.params.scenarioId) {
         tmp = window.sessionStorage.getItem("scenarioId")
      }
      else {
        tmp = this.$route.params.scenarioId;
        window.sessionStorage.setItem("scenarioId",this.$route.params.scenarioId);
      } 
      var tmpcol;
      if (!this.$route.params.collectionId) {
         tmpcol = window.sessionStorage.getItem("collectionId")
      }
      else {
        tmpcol = this.$route.params.collectionId;
        window.sessionStorage.setItem("collectionId",this.$route.params.collectionId);
      } 

      this.scenarioId = tmp;
      this.collectionId = tmpcol;
      const response = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+tmp+'/').catch(function (error) {
			console.log(error)
			return error.response.data;});
			console.log(response)
			if (response.status==200) {
                this.scenarioId = response.data.id;
                this.scenarioName = response.data.title;
                this.url = this.GLOBAL.baseURL+ response.data.img;
                this.scenarioDescription = response.data.description;
                this.createdDate = response.data.created;
                this.updatedDate = response.data.updated;
      }

      const response_dev = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+tmp+'/collections/'+tmpcol+'/devlinks/').catch(function (error) {
			console.log(error)
			return error.response_dev.data;});
			console.log(response_dev)
			if (response_dev.status==200) {
                this.devlinks = response_dev.data.reverse();
      }

      this.getDevCollection();

       const response1 = await this.axios.get(this.GLOBAL.baseURL+'/devices/').catch(function (error) {
			console.log(error)
            return error.response1.data;});

      this.options1 = response1.data;

      
  },
	methods:{

        popupActiveDev(tag){
            this.popupActiveDev_del=true;
            this.devlinkid = tag.devlink_id;
        },

        async deldevlink(devlinkid){
            var colid = this.collectionId;
         var sceid = this.scenarioId;
         var url = this.GLOBAL.baseURL+'/scenarios/'+sceid+'/collections/'+colid+'/devlinks/'+devlinkid+'/';
                  this.popupActiveDev_del=false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          //删除数组中的元素
          this.devlinks.forEach(function(item, index, arr) {
                if(item.devlink_id == devlinkid) {
                    arr.splice(index, 1);
                }
            });

          return true;
        },


        select_changed(){
        if (this.select1!='') {
            this.select_danger = false;
        }
        
        return true;
    },

        device_details(param) {
      this.$router.push({ name: 'deviceDetails', params: { deviceId: param }});

    },

        async getDevCollection(){

        const response = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/').catch(function (error) {
			console.log(error)
      return error.response.data;});
      if (response.status == 200 && response.data != ''){
        this.devcollection = response.data;
        //alert(JSON.stringify(response_tpltags.data));
       
      }
      },

      async adddevlink(){
          var devid = this.select1;

         if (this.select1=='') {
             this.select_danger=true;
             return true;
         }

         var params ={'device':devid,'collection':this.collectionId,'owner':1}

         const response = await this.axios.post(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/devlinks/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
            console.log(response)
        
        const response_dev = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/devlinks/').catch(function (error) {
			console.log(error)
			return error.response_dev.data;});
			console.log(response_dev)
			if (response_dev.status==200) {
                this.devlinks = response_dev.data.reverse();
      }
      },

      async addsetting(){

        if(this.settingTitle !='' && this.settingDescript!=''){

            var params ={'title':this.settingTitle,'collection':this.collectionId,'description':this.settingDescript}

            const response = await this.axios.post(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/ctrlsettings/',params).catch(function (error) {
                        console.log(error)
                return error.response.data;});
                console.log(response);
              const response1 = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/ctrlsettings/').catch(function (error) {
          console.log(error)
          return error.response1.data;});
          this.settingList = response1.data.reverse();
          this.settingTitle='';
          this.settingDescript='';
        }
          else{
          this.$vs.notify({
            title:'提醒：',
            text:'设备组合设置名称、描述都不能为空.',
            color:'danger'
          })
		}

      },

      async initsettings(){
        const response = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/ctrlsettings/').catch(function (error) {
			console.log(error)
      return error.response.data;});
      this.settingList = response.data.reverse();

      

      },

      async show_ctrlchannel(param){
        this.showctrlchannel = true;
        this.showsettingtitle = param.title;
        this.showsettingdescription = param.description;
        this.showsettingid = param.id;
        this.selected_linkchannels = [];

        const response = await this.axios.get(this.GLOBAL.baseURL+'/linkctrlchannels/').catch(function (error) {
        console.log(error)
        return error.response.data;});
        for(let tmpindex in response.data) {
          if(response.data[tmpindex].setting_id == param.id) {
            this.selected_linkchannels.push(response.data[tmpindex])
          }
        }

        this.linkchannels = [];
        
        for(let index in this.devlinks) {

          const response1 = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.devlinks[index].device_id+'/ctrlchannels/').catch(function (error) {
            console.log(error)
            return error.response1.data;});
            for(let tmp in response1.data){
              for(let tmpp in this.selected_linkchannels){
                if(response1.data[tmp].id == this.selected_linkchannels[tmpp].channel_id){
                  response1.data.splice(tmp,1);
                }
              } 
            this.linkchannels.push(response1.data[tmp]);
            }

        }

      },

      async addlinkctrlchannel(){

        for(let tmp in this.selected){

          var params ={'ctrlsetting':this.showsettingid,'ctrlchannel':this.selected[tmp].id,'owner':1}

         const response = await this.axios.post(this.GLOBAL.baseURL+'/linkctrlchannels/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
            console.log(response.data);
            for (let linktmp in this.linkchannels) {
              if(this.linkchannels[linktmp].id == this.selected[tmp].id){
                this.linkchannels.splice(linktmp,1)
              }
            }
          // this.linkchannels.forEach(function(item, index, arr) {
          //       if(item.id == response.data.channel_id) {
          //           arr.splice(index, 1);
          //       }
          //   });
        }


        const response = await this.axios.get(this.GLOBAL.baseURL+'/linkctrlchannels/').catch(function (error) {
        console.log(error)
        return error.response.data;});
        this.selected_linkchannels = [];
        for(let tmpindex in response.data) {
          if(response.data[tmpindex].setting_id == this.showsettingid) {
            this.selected_linkchannels.push(response.data[tmpindex])
          }
        }

        this.selected = [];
        

      },

      popupActiveSet(tag){
        this.popupActiveSet_del = true;
        this.tmp_setting = tag.id;


      },
      async delctrlset(tmp_setting){
        var url = this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/ctrlsettings/'+tmp_setting+'/';
        this.popupActiveSet_del = false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          
          //删除数组中的元素
          this.settingList.forEach(function(item, index, arr) {
                if(item.id == tmp_setting) {
                    arr.splice(index, 1);
                }
            });
          return true;

      },

      popupActiveSet_updatefunc(tag){

        this.popupActiveSet_update=true;
        this.settitle_input = tag.title;
        this.setdescript_input = tag.description;
        this.tmp_setting = tag.id;

      },

      async ctrlsetting_update(tmp_setting){

         var params = {"title":this.settitle_input,"description":this.setdescript_input};
         const response = await this.axios.patch(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/'+this.collectionId+'/ctrlsettings/'+tmp_setting+'/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});

              //删除数组中的元素
          this.settingList.forEach(function(item, index, arr) {
                if(item.id == response.data.id) {
                    arr.splice(index, 1,response.data);
                }
            });

          this.popupActiveSet_update=false;
          
          return true;
      },

      popupActiveSet_addparam(tr){
        this.popupActiveSet_addsetparam = true;
        this.linkchn_tmpid = tr.id;
        this.setparamkey_input = '';
        this.setparamvalue_input = '';

      },

      async ctrlsetting_addparam(linkchn_tmpid){

        var params ={'linkctrlchannel':linkchn_tmpid,'key':this.setparamkey_input,'value':this.setparamvalue_input}

         const response = await this.axios.post(this.GLOBAL.baseURL+'/linkctrlchannels/'+linkchn_tmpid+'/ctrlchannelparams/',params).catch(function (error) {
                    console.log(error)
            return error.response.data;});
            console.log(response.data);
         alert('添加成功，继续添加');
         this.setparamkey_input='';
         this.setparamvalue_input='';

      },

      async popupActiveSet_viewparam(tr){
        this.popupActiveSet_viewsetparam=true;
        this.linkchn_tmpid = tr.id;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/linkctrlchannels/'+this.linkchn_tmpid+'/ctrlchannelparams/').catch(function (error) {
        console.log(error)
        return error.response.data;});
        this.paramList = response.data;


      },

      handleSelected(tr) {
      this.$vs.notify({
        title: `Selected ${tr.title}`,
        text: `设备: ${tr.device}`
      })
    },

    popupActiveLinkCtrl(tr){
      this.popupActiveLinkCtrl_del=true;
      this.tmp_linkctrl=tr.id;
    },

    async dellinkctrl(tmp_linkctrl){
        var url = this.GLOBAL.baseURL+'/linkctrlchannels/'+tmp_linkctrl+'/';
        this.popupActiveLinkCtrl_del = false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          
          //删除数组中的元素
          this.selected_linkchannels.forEach(function(item, index, arr) {
                if(item.id == tmp_linkctrl) {
                    arr.splice(index, 1);
                }
            });
          return true;
    },

    async oneButtonControl(tag){
        const response = await this.axios.get(this.GLOBAL.baseURL+'/linkctrlchannels/').catch(function (error) {
        console.log(error)
        return error.response.data;});
        for(let tmpindex in response.data) {
          if(response.data[tmpindex].setting_id == tag.id) {
            this.selected_linkchannels_ctrl.push(response.data[tmpindex])
          }
        }

        for(let tmplinkctrl in this.selected_linkchannels_ctrl){
            const response1 = await this.axios.get(this.GLOBAL.baseURL+'/linkctrlchannels/'+this.selected_linkchannels_ctrl[tmplinkctrl].id+'/ctrlchannelparams/').catch(function (error) {
            console.log(error)
            return error.response1.data;});
            var params = {};
            for(let tmpparam in response1.data) {
                var tmp1 = response1.data[tmpparam].key;
                var tmp2 = response1.data[tmpparam].value;
                params[tmp1]=tmp2;
              }
            if(this.selected_linkchannels_ctrl[tmplinkctrl].channel_datatype=='DECIMAL'){
              
              const response2 = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+this.selected_linkchannels_ctrl[tmplinkctrl].device_id+'/ctrlchannels/'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_id+'/metricdata/',params).catch(function (error) {
                    console.log(error)
                  return error.response2.data;});
                  console.log(response2.data);
                  alert(this.selected_linkchannels_ctrl[tmplinkctrl].device_title+'--'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_title+'--'+'数值指令控制成功')
            }

            else if(this.selected_linkchannels_ctrl[tmplinkctrl].channel_datatype=='SWITCH'){

              const response3 = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+this.selected_linkchannels_ctrl[tmplinkctrl].device_id+'/ctrlchannels/'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_id+'/switchdata/',params).catch(function (error) {
                    console.log(error)
                  return error.response3.data;});
                  console.log(response3.data);
                  alert(this.selected_linkchannels_ctrl[tmplinkctrl].device_title+'--'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_title+'--'+'开关指令控制成功')
              
            }
            else if(this.selected_linkchannels_ctrl[tmplinkctrl].channel_datatype=='GPS'){

              const response4 = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+this.selected_linkchannels_ctrl[tmplinkctrl].device_id+'/ctrlchannels/'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_id+'/gpsdata/',params).catch(function (error) {
                    console.log(error)
                  return error.response4.data;});
                  console.log(response4.data);
                  alert(this.selected_linkchannels_ctrl[tmplinkctrl].device_title+'--'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_title+'--'+'GPS指令控制成功')
              
            }
            else if(this.selected_linkchannels_ctrl[tmplinkctrl].channel_datatype=='MESSAGE'){

              const response5 = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+this.selected_linkchannels_ctrl[tmplinkctrl].device_id+'/ctrlchannels/'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_id+'/textdata/',params).catch(function (error) {
                    console.log(error)
                  return error.response5.data;});
                  console.log(response5.data);
                  alert(this.selected_linkchannels_ctrl[tmplinkctrl].device_title+'--'+this.selected_linkchannels_ctrl[tmplinkctrl].channel_title+'--'+'文本指令控制成功')
            }
            else{
              alert('没有控制指令')
            }
        }
        this.selected_linkchannels_ctrl = [];
    },

	},

	
}
</script>
