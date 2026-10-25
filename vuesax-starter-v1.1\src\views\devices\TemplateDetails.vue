<template>
  <div class="mt-5">
    <vs-tabs vs-alignment="fixed" >
      <vs-tab vs-label="基本信息">
        <div>
          <div class="flex flex-wrap">
            <div class="w-full sm:w-1/2 md:w-1/3">
            <vx-card class="overlay-card overflow-hidden">
                <img :src=url alt="" slot="no-body" class="responsive card-img-top">

                <div class="w-full">
                <h5 style="text-align:center;"><span class="text-success" > 模板标签 </span></h5>
                <vs-divider/>
            <br>
            <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="标签key" v-model="tplTagKey" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="标签value" v-model="tplTagValue" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-button color="success" type="border" v-on:click="addtpltags(templateId)">添加</vs-button>
              </vs-col>
            </vs-row>
                
                </div>
                <vs-divider/>
                <vs-row vs-justify="center">
                <vs-table max-items="5" pagination :data="tplTagList">

                <template slot="thead">
                  <vs-th>序号</vs-th>
                  <vs-th>Key</vs-th>
                  <vs-th>Value</vs-th>
                  <div style="padding-left:30%;">
                  <vs-th>操作</vs-th>
                  </div>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td>
                      {{ indextag+1 }}
                    </vs-td>

                    <vs-td :data="data[indextag].key">
                      {{ data[indextag].key }}
                    </vs-td>

                    <vs-td :data="data[indextag].value">
                      {{ data[indextag].value }}
                    </vs-td>
                    <vs-td>
                            <vs-row>
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveTag1(tag,indextag)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑模板标签" :active.sync="popupActiveTag" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     标签Key：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                       <vs-input class="inputx" v-model="tagkey_input"/>
                                    </vs-col> 
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     标签Value：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                       <vs-input class="inputx" v-model="tagvalue_input"/>
                                    </vs-col> 
                                    <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      <vs-button color="success" type="border" @click="tpltag_update({'tmp_tag_param':tmp_tag,'tmp_tag_index_param':tmp_tag_index})">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <vx-tooltip color="danger" text="删除">
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveTag2(tag,indextag)"> </vs-button>
                                  <vs-popup class="holamundo"  title="删除模板标签" :active.sync="popupActiveTag_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="deltpltag({'tmp_tag_param':tmp_tag,'tmp_tag_index_param':tmp_tag_index})">确认删除</vs-button>
                                     </vs-col>

                                     <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActiveTag_del=false">取消</vs-button>
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
              </vs-row>
                
            </vx-card>

            </div>
            
             <div class="w-full sm:w-1/2 md:w-2/3 px-2">
             <vx-card class="overlay-card overflow-hidden">
              
            <p>模板名称： <span class="text-success" > {{ templateName }} </span></p>
            <br>
            <p>模板ID： {{ templateId }} </p>
            <p>设备型号： {{ deviceType }} </p>
            <!-- <p>协议类型： {{ protocalType }} </p> -->
            
            <p>是否允许设备发起注册： <span class="text-success" v-if = "is_reg">允许</span> <span class="text-warning" v-else>不允许</span></p>
            <br>
            <p>模板描述：</p>
            <p>{{ templateDescription }}</p>
            <br>
            <p>创建时间：{{ createdDate | formatDate }}</p>
            <p>更新时间：{{ updatedDate | formatDate  }}</p>


            </vx-card>
 
            </div>


            </div>
        </div>
      </vs-tab>
      <vs-tab vs-label="数据通道" @click="initchannel()"> 
          <div class="flex flex-wrap">
            <div class="w-full sm:w-1/2 md:w-2/4">
            <vx-card class="overlay-card overflow-hidden">
              <vs-row>
                <vs-col>
            <h6><span class="text-success">数据上传通道：</span>数据点，上传数据</h6>
            
                </vs-col>
              </vs-row>
            <br>
            <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="通道名称" v-model="datachannelName" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-select autocomplete class="selectExample" v-model="select1_datatype">
                  <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options1" />
                </vs-select>
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-button color="success" type="border" v-on:click="addtpldatachannel">添加</vs-button>
              </vs-col>
            </vs-row>
            <br>
            <vs-divider position="center">数据上传通道列表</vs-divider>
            <vs-col>
              <vs-table :data="tmpdataChannel"  pagination max-items="5" >

                <template slot="thead">
                  <vs-th>通道名称</vs-th>
                  <vs-th>ID号</vs-th>
                  <vs-th>数据类型</vs-th>
                  <vs-th  style="padding-left:20px;">单位</vs-th> 
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextr" v-for="(tr, indextr) in data" >                   
                  
                    <!-- <vs-td :data="data[indextr].title">
                      {{ data[indextr].title }}
                    </vs-td> -->

                     <vs-td :data="data[indextr].title">
                      {{ tr.title }}
                    </vs-td>

                    <vs-td :data="data[indextr].id">
                      {{ data[indextr].id }}
                    </vs-td>

                    <vs-td :data="data[indextr].datatype">

                      <div v-if="data[indextr].datatype === 'DECIMAL'">
                        数值型
                      </div>
                      <div v-else-if="data[indextr].datatype === 'MESSAGE'">
                        文本型
                      </div>
                      <div v-else-if="data[indextr].datatype === 'SWITCH'">
                        开关型
                      </div>
                      <div v-else>
                        GPS型
                      </div>

                      </vs-td>
                      <vs-td>
                       <!-- <div  hidden>{{ tpldataunit({'tplid':templateId,'chid':data[indextr].id}) }}</div> -->

                        <div v-if="data[indextr].datatype === 'DECIMAL'">


                          <div  style="margin-left:12px;" v-if="tr.unitsymbol">
                           {{ tr.unitsymbol }}
                           </div>  
                     
                          <!-- <div :key="indexunit" v-for="(xx,indexunit) in tplDataUnits" style="text-align:center;"> 
                              <div v-if="tr.id === xx.tpldatachannel">
                              {{ xx.symbol }}
                              </div> 
                          </div>  -->
                             
                          
                           
                            <div v-else>
                           <span class="text-success"> 
                                <!-- <vx-tooltip color="primary" text="添加数据单位"> -->
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-plus"  @click="popupActiveF2(tr,indextr)"></vs-button>
                                   <vs-popup class="holamundo"  title="添加数据单位" :active.sync="popupActive2" background-color="rgba(0,0,0,.1)">
                                     
                                         <div class="vx-col md:w-2/2 w-full mb-base"> 
                                         <vx-card>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>单位名称</span>
                                          </div>
                                          <div class="vx-col sm:w-2/3 w-full">
                                            <vs-input class="w-full" v-model="unitlabel" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>单位符号</span>
                                          </div>
                                          <div class="vx-col sm:w-2/3 w-full">
                                            <vs-input class="w-full" v-model="unitsymbol" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>最大值</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="maxvalue" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>最小值</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="minvalue" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>步长</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="unitstep" />
                                          </div>
                                        </div>

                                        <div class="vx-row">
                                          <div class="vx-col sm:w-2/3 w-full ml-auto">
                                            <vs-button class="mr-3 mb-2"  @click="adddataunit({'devtplid':tr.devtemplate,'tpl_dataid':tmp_dataid})">添加</vs-button>
                                            <vs-button color="warning" type="border" class="mb-2" @click="unitlabel=''; unitsymbol=''; unitstep=1;maxvalue=100;minvalue=1;">重置</vs-button>
                                          </div>
                                        </div>
                                      </vx-card>
                                    </div>
                                   
                                  </vs-popup>
                                <!-- </vx-tooltip> -->
                           </span>
                           </div> 
                           </div>
                          

                        <div v-else>
                          <span class="text-dark"> 
                                <vx-tooltip color="dark" text="无单位">
                                  <vs-button disabled  radius color="dark" type="flat" icon-pack="feather" icon="icon-minus"></vs-button>
                                </vx-tooltip>
                           </span>
                        </div>
                         
                      </vs-td>


                    <vs-td>

                          <vs-row>
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveF(tr,indextr)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑数据上传通道" :active.sync="popupActive1" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     通道名称：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                       <vs-input class="inputx" v-model="tmp_datach_title" />
                                    </vs-col> <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      <vs-button color="success" type="border" v-on:click="tmp_datach_update({'devtplid':tr.devtemplate,'tpl_dataid':tmp_dataid})">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <!-- <vx-tooltip color="danger" text="删除"> -->
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="deldatachannel({'tplid':templateId,'chid':data[indextr].id,'tmpid':data[indextr]})"> </vs-button>
                                <!-- </vx-tooltip> -->
                              </span>
                            </vs-col>


                          </vs-row>
        
                    </vs-td>
                  </vs-tr>
                  
                </template>
                
              </vs-table>
              <br>
            </vs-col>
            
  
            </vx-card>
            </div>
             <div class="w-full sm:w-1/2 md:w-2/4 px-1">
             <vx-card class="overlay-card overflow-hidden">
              <vs-row>
                <vs-col>
            <h6><span class="text-success">双向控制通道：</span>控制点，下发指令数据、上传状态数据</h6>
            
                </vs-col>
              </vs-row>
            <br>
             <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="通道名称" v-model="ctrlchannelName" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-select autocomplete class="selectExample" v-model="select2_datatype">
                  <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options2" />
                </vs-select>
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-button color="success" type="border" v-on:click="addtplctrlchannel">添加</vs-button>
              </vs-col>
            </vs-row>
            <br>
            <vs-divider position="center">双向控制通道列表</vs-divider>

            <vs-col>
              <vs-table :data="ctrlChannel"  pagination max-items="5" >

                <template slot="thead">
                  <vs-th>通道名称</vs-th>
                  <vs-th>ID号</vs-th>
                  <vs-th>数据类型</vs-th>
                  <vs-th >单位</vs-th> 
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextr" v-for="(tr, indextr) in data" >                   
                  
                    <!-- <vs-td :data="data[indextr].title">
                      {{ data[indextr].title }}
                    </vs-td> -->

                     <vs-td :data="data[indextr].title">
                      {{ tr.title }}
                    </vs-td>

                    <vs-td :data="data[indextr].id">
                      {{ data[indextr].id }}
                    </vs-td>

                    <vs-td :data="data[indextr].datatype">

                      <div v-if="data[indextr].datatype === 'DECIMAL'">
                        数值型
                      </div>
                      <div v-else-if="data[indextr].datatype === 'MESSAGE'">
                        文本型
                      </div>
                      <div v-else-if="data[indextr].datatype === 'SWITCH'">
                        开关型
                      </div>
                      <div v-else>
                        GPS型
                      </div>

                      </vs-td>
                      <vs-td>
                   
                        <div v-if="data[indextr].datatype === 'DECIMAL'">


                          <div v-if="tr.unitsymbol" style="text-align:center;" >
                           {{ data[indextr].unitsymbol }}
                           </div>  
                     
                          <!-- <div :key="indexunit" v-for="(xx,indexunit) in tplDataUnits" style="text-align:center;"> 
                              <div v-if="tr.id === xx.tpldatachannel">
                              {{ xx.symbol }}
                              </div> 
                          </div>  -->
                             
                          
                           
                            <div v-else>
                           <span class="text-success"> 
                                <!-- <vx-tooltip color="primary" text="添加数据单位"> -->
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-plus"  @click="popupActiveF2ctrl(tr,indextr)"></vs-button>
                                   <vs-popup class="holamundo"  title="添加数据单位" :active.sync="popupActive2ctrl" background-color="rgba(0,0,0,.1)">
                                     
                                         <div class="vx-col md:w-2/2 w-full mb-base"> 
                                         <vx-card>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>单位名称</span>
                                          </div>
                                          <div class="vx-col sm:w-2/3 w-full">
                                            <vs-input class="w-full" v-model="unitlabel" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>单位符号</span>
                                          </div>
                                          <div class="vx-col sm:w-2/3 w-full">
                                            <vs-input class="w-full" v-model="unitsymbol" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>最大值</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="maxvalue" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>最小值</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="minvalue" />
                                          </div>
                                        </div>
                                        <div class="vx-row mb-6">
                                          <div class="vx-col sm:w-1/3 w-full">
                                            <span>步长</span>
                                          </div>
                                          <div class="vx-col">
                                            <vs-input-number color="success" v-model="unitstep" />
                                          </div>
                                        </div>

                                        <div class="vx-row">
                                          <div class="vx-col sm:w-2/3 w-full ml-auto">
                                            <vs-button class="mr-3 mb-2"  @click="addctrlunit({'devtplid':tr.devtemplate,'tpl_ctrlid':tmp_ctrlid})">添加</vs-button>
                                            <vs-button color="warning" type="border" class="mb-2" @click="unitlabel=''; unitsymbol=''; unitstep=1;maxvalue=100;minvalue=1;">重置</vs-button>
                                          </div>
                                        </div>
                                      </vx-card>
                                    </div>
                                   
                                  </vs-popup>
                                <!-- </vx-tooltip> -->
                           </span>
                           </div> 
                           </div>
                          

                        <div v-else>
                          <span class="text-dark"> 
                                <vx-tooltip color="dark" text="无单位">
                                  <vs-button disabled  radius color="dark" type="flat" icon-pack="feather" icon="icon-minus"></vs-button>
                                </vx-tooltip>
                           </span>
                        </div>
                         
                      </vs-td>


                    <vs-td>

                          <vs-row>
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveFctrl(tr,indextr)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑双向控制通道" :active.sync="popupActive1ctrl" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     通道名称：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                       <vs-input class="inputx" v-model="tmp_ctrlch_title" />
                                    </vs-col> <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      <vs-button color="success" type="border" v-on:click="tmp_ctrlch_update({'devtplid':tr.devtemplate,'tpl_ctrlid':tmp_ctrlid})">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <!-- <vx-tooltip color="danger" text="删除"> -->
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="delctrlchannel({'tplid':templateId,'chid':data[indextr].id,'tmpid':data[indextr]})"> </vs-button>
                                <!-- </vx-tooltip> -->
                              </span>
                            </vs-col>


                          </vs-row>
        
                    </vs-td>
                  </vs-tr>
                  
                </template>
                
              </vs-table>
              <br>
            </vs-col>

            </vx-card>
 
            </div>
        </div>
      </vs-tab>


    </vs-tabs>
  </div>

  
</template>

<script>

var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}

export default {
    data() {
        return {
            url:'',
            templateName:'',
            templateId:'',
            templateDescription:'',
            deviceType:'',
            protocalType:'',
            is_reg:'',
            createdDate:'',
            updatedDate:'',
            dataChannel: [],
            tmpdataChannel:[],

            tplDataUnits: [

            ],

            select1_datatype:'DECIMAL',
            options1:[
              {text:'数值型',value:'DECIMAL'},
              {text:'开关型',value:'SWITCH'},
              {text:'文本型',value:'MESSAGE'},
              {text:'GPS型',value:'GPS'},
            ],
            datachannelName:'',
            popupActive1: false,
            tmp_dataid:'',
            tmp_datach_title:'',
            index_tmp:'',
            index_tmp2:'',
            popupActive2: false,
            //unit
            unitlabel:'',
            unitsymbol:'',
            unitstep:1,
            maxvalue:100,
            minvalue:1,
            // template tags 
            tplTagKey:'',
            tplTagValue:'',
            tplTagList:[],
            popupActiveTag:false,
            tagkey_input:'',
            tagvalue_input:'',
            tmp_tag_index:'',
            tmp_tag:'',
            popupActiveTag_del:false,
            // control channel
            ctrlChannel: [],
            tmpctrlChannel:[],
            ctrlchannelName:'',
            select2_datatype:'DECIMAL',
            options2:[
              {text:'数值型',value:'DECIMAL'},
              {text:'开关型',value:'SWITCH'},
              {text:'文本型',value:'MESSAGE'},
              {text:'GPS型',value:'GPS'},
            ],
            popupActive1ctrl: false,
            tmp_ctrlid:'',
            tmp_ctrlch_title:'',
            index_tmpctrl:'',
            popupActive2ctrl: false,
            index_tmp2ctrl:'',
            tplCtrlUnits: [

            ],
          
        }
    },

    mounted: async function() {
      var tmp;
      if (!this.$route.params.templateId) {
         tmp = window.sessionStorage.getItem("templateId")
      }
      else {
        tmp = this.$route.params.templateId;
        window.sessionStorage.setItem("templateId",this.$route.params.templateId);
      } 
      const response = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/').catch(function (error) {
			console.log(error)
			return error.response.data;});
			console.log(response)
			if (response.status==200) {
                this.templateId = response.data.id;
                this.templateName = response.data.title;
                this.url = this.GLOBAL.baseURL+ response.data.img;
                this.templateDescription = response.data.description;
                this.deviceType = response.data.device_type;
                this.protocalType = response.data.protocal_type;
                this.is_reg = response.data.is_custom_registered;
                this.createdDate = response.data.created;
                this.updatedDate = response.data.updated;
      }

      //template tags list
      const response_tpltags = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/templatetags/').catch(function (error) {
			console.log(error)
      return error.response_tpltags.data;});
      if (response_tpltags.status == 200 && response_tpltags.data != ''){
        this.tplTagList = response_tpltags.data;
        //alert(JSON.stringify(response_tpltags.data));
       
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

     methods:{

       popupActiveTag1(param1,param2){
         this.popupActiveTag=true;
         this.tmp_tag = param1;
         this.tagkey_input = param1.key;
         this.tagvalue_input = param1.value;
         this.tmp_tag_index = param2;

       },
       popupActiveTag2(param1,param2){
         this.popupActiveTag_del=true;
         this.tmp_tag = param1;
         this.tagkey_input = param1.key;
         this.tagvalue_input = param1.value;
         this.tmp_tag_index = param2;

       },

       
       popupActiveF(param,param2) {

         this.popupActive1=true;
         this.tmp_dataid = param;
         this.tmp_datach_title = param.title;
         this.index_tmp = param2;    

       },
       popupActiveF2(param,param2) {
  
         this.popupActive2=true;
         this.tmp_dataid = param.id; 
         this.index_tmp2 = param2;
       },

       async addtpltags(param) {
         //alert(param);
         if(this.tplTagKey!='' && this.tplTagValue!=''){
            var params ={"devtemplate":param,"key":this.tplTagKey,"value":this.tplTagValue}
            const response = await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/'+param+'/templatetags/',params).catch(function (error) {
            console.log(error)
            return error.response.data;});
            if(response.status == 201){
              //insert first 
              this.tplTagList.splice(0,0,response.data);
              //alert(JSON.stringify(response.data));
              this.tplTagKey='';
              this.tplTagValue='';
            }
         }
         else{
           this.$vs.notify({
            title:'提醒：',
            text:'标签key，标签value值都不能为空.',
            color:'danger'
          })
         }
        
        //alert(JSON.stringify(response.data));

       },

       async tmp_datach_update(param) {
         if(this.tmp_datach_title!=''){
            var devtplid = param.devtplid;
            var tpl_dataid=param.tpl_dataid.id;
            var params = {"title":this.tmp_datach_title};

            const response = await this.axios.patch(this.GLOBAL.baseURL+'/devtemplates/'+devtplid+'/tpldatachannels/'+tpl_dataid+'/',params).catch(function (error) {
                  console.log(error)
                  return error.response.data;});
            
            this.popupActive1 = false;

            this.tmpdataChannel.forEach(function(item, index, arr) {
                    if(item.id == tpl_dataid) {
                        arr.splice(index, 1,response.data);
                    }
                });
         }
         else{
           this.$vs.notify({
            title:'提醒：',
            text:'通道名称不能为空.',
            color:'danger'
          })

         }
       },

       async adddataunit(param) {

         if(this.unitlabel!='' &&this.unitsymbol!='' ){
         
            var devtplid = param.devtplid;
            var tpl_dataid =param.tpl_dataid;
            this.popupActive2 =  false;
            var params ={"tpldatachannel":tpl_dataid,"unitlabel":this.unitlabel,"symbol":this.unitsymbol,"max_value":this.maxvalue,"min_value":this.minvalue,"step":this.unitstep}
            const response = await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/'+devtplid+'/tpldatachannels/'+tpl_dataid+'/tpldataunits/',params).catch(function (error) {
            console.log(error)
            return error.response.data;});

            this.tplDataUnits.push(response.data);
            //alert(JSON.stringify(this.tplDataUnits));

            //删除数组中的元素
              this.tmpdataChannel.forEach(function(item, index, arr) {
                    if(item.id == tpl_dataid) {
                      arr[index].unitsymbol = response.data.symbol;
                      return true;
            
                    }
                });
            // this.tmpdataChannel=this.dataChannel;
            //window.location.reload();
         }
         else {
           this.$vs.notify({
            title:'提醒：',
            text:'单位名称、单位符号都不能为空.',
            color:'danger'
          })
         }

       },


      //    async tpldataunit(param) {

      //     var tmp_devtmp= param.tplid;
      //     var tmp_unit = param.chid;
          
      //     const response = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp_devtmp+'/tpldatachannels/'+tmp_unit+'/tpldataunits/').catch(function (error) {
      //     console.log(error);
      //     return error.response.data;});
      //     if (response.status == 200) {
      //               //return response.data[0].symbol;
      //               this.dataChannelunitsymbol[tmp_unit] =  response.data[0].symbol     
      //     }

      //  },

      //  async tplctrlunit(param) {

      //     var tmp_devtmp= param.tplid;
      //     var tmp_unit = param.chid;
          
      //     const response = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp_devtmp+'/tplctrlchannels/'+tmp_unit+'/tplctrlunits/').catch(function (error) {
      //     console.log(error);
      //     return error.response.data;});
      //     if (response.status == 200) {
      //               //return response.data[0].symbol;
      //               this.ctrlChannelunitsymbol[tmp_unit] =  response.data[0].symbol     
      //     }

      //  },

       async addtpldatachannel() {
          var tmp;
          if (!this.$route.params.templateId) {
            tmp = window.sessionStorage.getItem("templateId")
          }
          else {
            tmp = this.$route.params.templateId;
            window.sessionStorage.setItem("templateId",this.$route.params.templateId);
          } 

          if (this.datachannelName) {

              var params = {"devtemplate":tmp,"title":this.datachannelName,"datatype":this.select1_datatype};

              const response = await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tpldatachannels/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});
              if (response.status==201) {
                this.dataChannel.unshift(response.data);
                this.datachannelName = '';
              } 
          }
          else {
            alert("通道名称不能为空！");
          }
          

       },

       async deldatachannel(param) {

          var tmp_devtmp= param.tplid;
          var tmp_datachn = param.chid;
          var tmp_delid = param.tmpid;

          var url = this.GLOBAL.baseURL+'/devtemplates/'+tmp_devtmp+'/tpldatachannels/'+tmp_datachn+'/';
          await this.axios.delete(url).then(function(response) {
            console.log(response);
            alert("已删除")
          });
           
          //删除数组中的元素
          this.dataChannel.forEach(function(item, index, arr) {
                if(item == tmp_delid) {
                    arr.splice(index, 1);
                }
            });
       },

       async tpltag_update(param){
         //alert(param.tmp_tag_param);
         //alert(param.tmp_tag_index_param);
         if(this.tagkey_input!='' && this.tagvalue_input!=''){
            var tagid = param.tmp_tag_param.id;
            var devtpl = param.tmp_tag_param.devtemplate;
            var tagkey = this.tagkey_input;
            var tagvalue = this.tagvalue_input;
            var tagindex = param.tmp_tag_index_param;
            var params = {"devtemplate":devtpl,"key":tagkey,"value":tagvalue};

            const response = await this.axios.patch(this.GLOBAL.baseURL+'/devtemplates/'+devtpl+'/templatetags/'+tagid+'/',params).catch(function (error) {
                  console.log(error)
                  return error.response.data;});
                  if (response.status==200) {
                    this.tplTagList[tagindex].key = response.data.key;
                    this.tplTagList[tagindex].value = response.data.value;
                    this.popupActiveTag = false;
                  }
         }
         else{
           this.$vs.notify({
            title:'提醒：',
            text:'标签key，标签value值都不能为空.',
            color:'danger'
          })
         }
        

       },

       async deltpltag(param){
         var tagid = param.tmp_tag_param.id;
         var devtpl = param.tmp_tag_param.devtemplate;
         var tagindex = param.tmp_tag_index_param;
         var url = this.GLOBAL.baseURL+'/devtemplates/'+devtpl+'/templatetags/'+tagid+'/';
                  this.popupActiveTag_del=false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
            alert("已删除");
          });
          //删除数组中的元素
          
         this.tplTagList.splice(tagindex,1);

       },

       //以下是控制通道

       async addtplctrlchannel() {
          var tmp;
          if (!this.$route.params.templateId) {
            tmp = window.sessionStorage.getItem("templateId")
          }
          else {
            tmp = this.$route.params.templateId;
            window.sessionStorage.setItem("templateId",this.$route.params.templateId);
          } 

          if (this.ctrlchannelName) {

              var params = {"devtemplate":tmp,"title":this.ctrlchannelName,"datatype":this.select2_datatype};

              const response = await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tplctrlchannels/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});
              if (response.status==201) {
                this.ctrlChannel.unshift(response.data);
                this.ctrlchannelName = '';
              } 
          }
          else {
            alert("通道名称不能为空！");
          }
       },

       popupActiveFctrl(param,param2) {

         this.popupActive1ctrl=true;
         this.tmp_ctrlid = param;
         this.tmp_ctrlch_title = param.title;
         this.index_tmpctrl = param2;    

       },

       async tmp_ctrlch_update(param) {

         if(this.tmp_ctrlch_title!=''){
            var devtplid = param.devtplid;
            var tpl_ctrlid=param.tpl_ctrlid.id;
            var params = {"title":this.tmp_ctrlch_title};

            const response = await this.axios.patch(this.GLOBAL.baseURL+'/devtemplates/'+devtplid+'/tplctrlchannels/'+tpl_ctrlid+'/',params).catch(function (error) {
                  console.log(error)
                  return error.response.data;});

            this.popupActive1ctrl = false;

            this.ctrlChannel.forEach(function(item, index, arr) {
                    if(item.id == tpl_ctrlid) {
                        arr.splice(index, 1,response.data);
                    }
                });
         }
         else{
           this.$vs.notify({
            title:'提醒：',
            text:'通道名称不能为空.',
            color:'danger'
          })
         }

       },

       async delctrlchannel(param) {

          var tmp_devtmp= param.tplid;
          var tmp_ctrlchn = param.chid;
          var tmp_delid = param.tmpid;

          var url = this.GLOBAL.baseURL+'/devtemplates/'+tmp_devtmp+'/tplctrlchannels/'+tmp_ctrlchn+'/';
          await this.axios.delete(url).then(function(response) {
            console.log(response);
            alert("已删除")
          });
           
          //删除数组中的元素
          this.ctrlChannel.forEach(function(item, index, arr) {
                if(item == tmp_delid) {
                    arr.splice(index, 1);
                }
            });
       },

       popupActiveF2ctrl(param,param2) {
  
         this.popupActive2ctrl=true;
         this.tmp_ctrlid = param.id; 
         this.index_tmp2ctrl = param2;
       },

       async addctrlunit(param) {

         if(this.unitlabel!='' && this.unitsymbol!=''){
         
            var devtplid = param.devtplid;
            var tpl_ctrlid =param.tpl_ctrlid;
            this.popupActive2ctrl =  false;
            //alert('dd');
            var params ={"tplctrlchannel":tpl_ctrlid,"unitlabel":this.unitlabel,"symbol":this.unitsymbol,"max_value":this.maxvalue,"min_value":this.minvalue,"step":this.unitstep}
            const response =await this.axios.post(this.GLOBAL.baseURL+'/devtemplates/'+devtplid+'/tplctrlchannels/'+tpl_ctrlid+'/tplctrlunits/',params).catch(function (error) {
            console.log(error)
            return error.response.data;});

              this.ctrlChannel.forEach(function(item, index, arr) {
                    if(item.id == tpl_ctrlid) {
                      arr[index].unitsymbol = response.data.symbol;
                      return true;
            
                    }
                });
            
            //window.location.reload();
         }
         else{
           this.$vs.notify({
            title:'提醒：',
            text:'单位名称、单位符号都不能为空.',
            color:'danger'
          })
         }

       },

       async initchannel(){

       var tmp;
      if (!this.$route.params.templateId) {
         tmp = window.sessionStorage.getItem("templateId")
      }
      else {
        tmp = this.$route.params.templateId;
        window.sessionStorage.setItem("templateId",this.$route.params.templateId);
      } 
         
      const response_datachannel = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tpldatachannels/').catch(function (error) {
			console.log(error)
			return error.response_datachannel.data;});
      console.log(response_datachannel)
      if (response_datachannel.status == 200) {
                this.dataChannel =  response_datachannel.data;
                
      }
      
      for(var tmp_index in this.dataChannel) {
        var tmp_channel_id = this.dataChannel[tmp_index].id;
       
        const response_unit = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tpldatachannels/'+tmp_channel_id+'/tpldataunits/').catch(function (error) {
			console.log(error)
      return error.response_unit.data;});
      if (response_unit.status == 200 && response_unit.data != ''){
        //alert(JSON.stringify(response_unit.data[0]));
        this.tplDataUnits.push(response_unit.data[0]);
        this.dataChannel[tmp_index].unitsymbol = response_unit.data[0].symbol;
        //alert(this.dataChannel[tmp_index].unitsymbol)
       
      }
      }
      this.tmpdataChannel = this.dataChannel;
      //alert(JSON.stringify(this.tplDataUnits));
      

      const response_ctrlchannel = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tplctrlchannels/').catch(function (error) {
			console.log(error)
			return error.response_ctrlchannel.data;});
      console.log(response_ctrlchannel)
      if (response_ctrlchannel.status == 200) {
                this.tmpctrlChannel =  response_ctrlchannel.data;
                
      }

      // display ctrl channel units
      for(var tmp_index1 in this.tmpctrlChannel) {
        var tmp_channel_id1 = this.tmpctrlChannel[tmp_index1].id;
       
        const response_unitctrl = await this.axios.get(this.GLOBAL.baseURL+'/devtemplates/'+tmp+'/tplctrlchannels/'+tmp_channel_id1+'/tplctrlunits/').catch(function (error) {
			console.log(error)
      return error.response_unitctrl.data;});
      if (response_unitctrl.status == 200 && response_unitctrl.data != ''){
        //alert(JSON.stringify(response_unitctrl.data[0]));
        this.tplCtrlUnits.push(response_unitctrl.data[0]);
        //alert('ddd');
        this.tmpctrlChannel[tmp_index1].unitsymbol = response_unitctrl.data[0].symbol;
        //alert(this.ctrlChannel[tmp_index1].unitsymbol);
        
       
      }
      }
      this.ctrlChannel = this.tmpctrlChannel;

       },


    },
  
  
}
</script>


