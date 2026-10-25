<template>
  <div class="mt-5">
    <vs-tabs vs-alignment="fixed" >
      <vs-tab vs-label="基本信息">
        <div>
          <div class="flex flex-wrap">
            <div class="w-full sm:w-1/2 md:w-1/3">
            <vx-card class="overlay-card overflow-hidden">
                <img :src=url alt="" slot="no-body" class="responsive card-img-top">
            </vx-card>

            </div>
            
             <div class="w-full sm:w-1/2 md:w-2/3 px-2">
             <vx-card class="overlay-card overflow-hidden">
              
            <p>应用场景名称： <span class="text-success" > {{ scenarioName }} </span></p>
            <br>
            <p>应用场景ID： {{ scenarioId }} </p>
            <br>
            <p>应用场景描述：</p>
            <p>{{ scenarioDescription }}</p>
            <br>

            <p>创建时间：{{ createdDate | formatDate }}</p>
            <p>更新时间：{{ updatedDate | formatDate  }}</p>
            <vs-divider> </vs-divider>
            <p><vs-button line-origin="left" color="success" type="line" @click="qrcodeinit()">显示二维码</vs-button></p>
            <br>
            <div id="qrcode"></div>
            </vx-card>
 
            </div>

            </div>
        </div>
      </vs-tab>
      <vs-tab vs-label="设备组合" @click="collectionlist()">
        <div>
          <div class="flex flex-wrap">
            <vs-row>
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card class="overlay-card overflow-hidden">
                  <vs-row>
                  <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="2">
                    <vs-input class="inputx w-full" placeholder="设备组合名称" v-model="devColTitle" />
                  </vs-col>
                  <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="6">
                    <vs-input class="inputx w-full" placeholder="设备组合描述" v-model="devColDescript" />
                  </vs-col>
                  <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                    <vs-button color="success" type="flat" icon-pack="feather" icon="icon-plus"  v-on:click="adddevcol(scenarioId)">添加设备组合</vs-button>
                  </vs-col>
                  </vs-row>
                  <vs-divider/>
                  <br>
                 <vs-table max-items="5" pagination :data="collectionList">

                <template slot="thead">
                  <vs-th>ID号</vs-th>
                  <vs-th>名称</vs-th>
                  <vs-th>描述</vs-th>
                  <div style="padding-left:20%;">
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
                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-file-text" v-on:click="collection_details(tag)"></vs-button>
                              </span>
                              
                            </vs-col>

                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveCol_updatefunc(tag)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑设备组合" :active.sync="popupActiveCol_update" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     设备组合名称：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-input class="inputx" v-model="devcoltitle_input"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     设备组合描述：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                       <vs-textarea class="inputx" v-model="devcoldescript_input"/>
                                    </vs-col> 
                                    <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                      <vs-button color="success" type="border" @click="devcol_update(tmp_col)">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                              <span class="text-danger"> 
                                <vx-tooltip color="danger" text="删除">
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveCol(tag)"> </vs-button>
                                  <vs-popup class="holamundo"  title="删除设备组合" :active.sync="popupActiveCol_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="danger" type="filled" @click="deldevcol(tmp_col)">确认删除</vs-button>
                                     </vs-col>
                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveCol_del=false">取消</vs-button>
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

                </vx-card>
              </vs-col>
            </vs-row>


            </div>
        </div>
      </vs-tab>

 

    </vs-tabs>
  </div>

  
</template>

<script>

import QRCode from 'qrcodejs2'

var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}

export default {
    data() {
        return {

            url:'',
            scenarioName:'',
            scenarioId:'',
            scenarioDescription:'',

            createdDate:'',
            updatedDate:'',
            collectionList:[],
            popupActiveCol_del:false,
            tmp_col:'',
            devColTitle:'',
            devColDescript:'',

            popupActiveCol_update:false,
            devcoltitle_input:'',
            devcoldescript_input:'',
           

          
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

      // this.qrcode();
      
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

     methods:{

      collection_details(param) {
			this.$router.push({ name: 'collectionDetails', params: { scenarioId: param.scenario,collectionId:param.id }})

		},

       qrcodeinit(){
         document.getElementById("qrcode").innerHTML = "";
         let qrcode = new QRCode('qrcode', {
        width: 150,
        height: 150, // 高度
        text: this.scenarioId,// 二维码内容
        correctLevel: QRCode.CorrectLevel.H
        // render: 'canvas' // 设置渲染方式（有两种方式 table和canvas，默认是canvas）
        // background: '#f0f'
        // foreground: '#ff0'
      })
      console.log(qrcode)

     },

       async collectionlist(){
        const response = await this.axios.get(this.GLOBAL.baseURL+'/scenarios/'+this.scenarioId+'/collections/').catch(function (error) {
        console.log(error)
        return error.response.data;});
        if (response.status == 200 && response.data != ''){
          this.collectionList = response.data.reverse();
        
        }
       },

       popupActiveCol(param1){
         this.popupActiveCol_del=true;
         this.tmp_col = param1.id;

       },

       popupActiveCol_updatefunc(param1){
         this.popupActiveCol_update=true;
         this.tmp_col = param1.id;
         this.devcoltitle_input=param1.title;
         this.devcoldescript_input=param1.description;

       },

       async deldevcol(param){
         var colid = param;
         var sceid = this.scenarioId;
         var url = this.GLOBAL.baseURL+'/scenarios/'+sceid+'/collections/'+colid+'/';
                  this.popupActiveCol_del=false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          //删除数组中的元素
          this.collectionList.forEach(function(item, index, arr) {
                if(item.id == colid) {
                    arr.splice(index, 1);
                }
            });

          return true;

       },

       async adddevcol(param) {
         //alert(param);
         if(this.devColTitle !='' && this.devColDescript !=''){
            var params ={"scenario":param,"title":this.devColTitle,"description":this.devColDescript}
            const response = await this.axios.post(this.GLOBAL.baseURL+'/scenarios/'+param+'/collections/',params).catch(function (error) {
            console.log(error)
            return error.response.data;});
            // if(this.collectionList==='') {
            //   this.collectionList.append(response.data);
            // }
            // if(response.status == 201){
              this.collectionList.unshift(response.data);
              //insert first 
              //this.collectionList.splice(0,0,response.data);
              //alert(JSON.stringify(response.data));
              this.devColTitle='';
              this.devColDescript='';
            // }
         }
         else{
          this.$vs.notify({
            title:'提醒：',
            text:'设备组合名称、描述都不能为空.',
            color:'danger'
          })
		}
        
        //alert(JSON.stringify(response.data));

       },


       async devcol_update(param){
         //alert(param.tmp_tag_param);
         //alert(param.tmp_tag_index_param);
         if(this.devcoltitle_input !='') {
            var colid = param;
            var sceid = this.scenarioId;
            var coltitle = this.devcoltitle_input;
            var coldescript = this.devcoldescript_input;
            var params = {"scenario":sceid,"title":coltitle,"description":coldescript};
            const response = await this.axios.patch(this.GLOBAL.baseURL+'/scenarios/'+sceid+'/collections/'+colid+'/',params).catch(function (error) {
                  console.log(error)
                  return error.response.data;});

                  //删除数组中的元素
              this.collectionList.forEach(function(item, index, arr) {
                    if(item.id == colid) {
                        arr.splice(index, 1,response.data);
                    }
                });

              this.popupActiveCol_update=false;
              
              return true;
         }
         else{
          this.$vs.notify({
            title:'提醒：',
            text:'设备组合名称不能为空.',
            color:'danger'
          })
		}

       },




    },
  
  
}
</script>


