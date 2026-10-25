<template>
  <div class="mt-5">
    <vs-tabs vs-alignment="fixed" >
      <vs-tab vs-label="基本信息" >
        <div>
          <div class="flex flex-wrap">
            <div class="w-full sm:w-1/2 md:w-1/3">
            <vx-card class="overlay-card overflow-hidden">
                <img :src=url alt="" slot="no-body" class="responsive card-img-top">

                <div class="w-full">
                <h5 style="text-align:center;"><span class="text-success" > 设备标签 </span></h5>
                <vs-divider/>
            <br>
            <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="标签key" v-model="devTagKey" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-input class="inputx" placeholder="标签value" v-model="devTagValue" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                <vs-button color="success" type="border" v-on:click="adddevtags(deviceId)">添加</vs-button>
              </vs-col>
            </vs-row>
                
                </div>
                <vs-divider/>
                <vs-row vs-justify="center">
                <vs-table max-items="5" pagination :data="devTagList"  class="responsive">

                <template slot="thead">
                  <vs-th>ID号</vs-th>
                  <vs-th>Key</vs-th>
                  <vs-th>Value</vs-th>
                  <vs-th>操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                    <vs-td :data="data[indextag].id">
                      {{ data[indextag].id }}
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

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveTag1(tag)"></vs-button>
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
                                      <vs-button color="success" type="border" @click="devtag_update(tmp_tag)">更新</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <vx-tooltip color="danger" text="删除">
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="popupActiveTag2(tag)"> </vs-button>
                                  <vs-popup class="holamundo"  title="删除设备标签" :active.sync="popupActiveTag_del" background-color="rgba(0,0,0,.1)">
                                    <vs-row  vs-justify="center">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      
                                     <vs-button color="danger" type="filled" @click="deldevtag(tmp_tag)">确认删除</vs-button>
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
              
            <p>设备名称： <span class="text-success" > {{ deviceName }} </span></p>
            <br>
            <p>设备ID： {{ deviceId }} </p>
            <p>设备型号： {{ deviceType }} </p>
            <!-- <p>协议类型： {{ protocalType }} </p> -->
            
            <p>是否允许设备发起注册： <span class="text-success" v-if = "is_reg">允许</span> <span class="text-warning" v-else>不允许</span></p>
            <br>
            <p>设备描述：</p>
            <p>{{ deviceDescription }}</p>
            <br>
            <p>注册码：{{ deviceRegCode }}</p>
            <p>设备状态：<span class="text-success" v-if="deviceStatus=='ACTIVE' || deviceStatus=='ONLINE' "> {{ deviceStatus }} </span><span class="text-warning" v-else>{{ deviceStatus }} </span></p>
            <br>
            <p>最新在线时间：<span v-if="onlinedDate===null">未曾联网</span><span v-else>{{ onlinedDate | formatDate }}</span></p>
            <p>设备激活时间：<span v-if="activatedDate===null">未曾激活</span><span v-else>{{ activatedDate | formatDate }}</span></p>

            <br>
            <p>创建时间：{{ createdDate | formatDate }}</p>
            <p>更新时间：{{ updatedDate | formatDate  }}</p>
            <vs-divider/>
            <p><vs-button line-origin="left" color="success" type="line" @click="qrcodeinit()">显示二维码</vs-button></p>
            <br>
            <div id="qrcode"></div>
            </vx-card>
 
            </div>

            </div>
        </div>
      </vs-tab>
      <vs-tab vs-label="上传通道"> 
          <div class="flex flex-wrap">
            <div class="w-full sm:w-2/2 md:w-4/4">
            <vx-card class="overlay-card overflow-hidden">
              <vs-row>
                <vs-col>
            <h5><span class="text-success">数据上传通道：</span>数据点用于上传数据</h5>
                </vs-col>
              </vs-row>
            <br>
            <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                <vs-input class="inputx" placeholder="通道名称" v-model="datachannelName" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                <vs-select autocomplete class="selectExample" v-model="select1_datatype">
                  <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options1" />
                </vs-select>
              </vs-col>
              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                <vs-button color="success" type="border" v-on:click="adddatachannel">添加</vs-button>
              </vs-col>
            </vs-row>
            <br>
            <vs-divider/>
            
            <vs-col>
              <vs-table :data="dataChannelTmp"  pagination max-items="5" >
                <template slot="thead">
                  <vs-th>通道名称</vs-th>
                  <vs-th>ID号</vs-th>
                  <vs-th>数据类型</vs-th>
                  <vs-th style="padding-left:20px;" >单位</vs-th> 
                  <vs-th >数据查看</vs-th> 
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :state="indextr == selectrow ? 'success':null"  :key="indextr" v-for="(tr, indextr) in data" >                   
                  
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
                          <div v-if="tr.unitsymbol" style="margin-left:15px;">
                           {{ tr.unitsymbol }}
                           </div>  
                     
                          <!-- <div :key="indexunit" v-for="(xx,indexunit) in tplDataUnits" style="text-align:center;"> 
                              <div v-if="tr.id === xx.tpldatachannel">
                              {{ xx.symbol }}
                              </div> 
                          </div>  -->
                             
                            <div v-else>
                           <span class="text-success"> 
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-plus"  @click="popupActiveF2(tr)"></vs-button>
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
                                            <vs-button class="mr-3 mb-2"  @click="adddataunit(tmp_dataid)">添加</vs-button>
                                            <vs-button color="warning" type="border" class="mb-2" @click="unitlabel=''; unitsymbol=''; unitstep=1;maxvalue=100;minvalue=1;">重置</vs-button>
                                          </div>
                                        </div>
                                      </vx-card>
                                    </div>
                                   
                                  </vs-popup>
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

                      <vs-td :data="data[indextr].datatype">

                      <div v-if="data[indextr].datatype === 'DECIMAL'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-bar-chart" @click="echartshowline(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                                <!-- <vs-popup fullscreen :title="deviceName" :active.sync="popupActiveLine">
                                  <vs-row>
                                    <vs-divider>
                                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
                                        <h3 class="text-success">{{tmp_datach_name}}</h3>
                                    </vs-col>
                                    </vs-divider>
                                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
                                        <div class="centerx">
                                          <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="6" >
                                              <vs-input class="inputx" placeholder="模拟数据" v-model="datach_datainput" />
                                          </vs-col>
                                          <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="6" >
                                             <vs-button color="success" type="border" icon-pack="feather" icon="icon-check" size="small">提交</vs-button>
                                          </vs-col>
                                        </div>
                                    </vs-col>
                                  </vs-row>
                                  <vs-divider/>
                                   <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                                              <div id="echartContainer2" style="width:500px; height:500px"></div>         
                                </vs-popup> -->
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'MESSAGE'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-message-circle" @click="echartshowmsgFun(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'SWITCH'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-toggle-left" @click="echartshowswitch(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else>
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-map-pin" @click="echartshowmapFun(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>

                      </vs-td>


                    <vs-td>

                          <vs-row>
                            <vs-col vs-type="flex" vs-w="4">
                              <span class="text-success"> 
                                <vx-tooltip color="primary" text="编辑"> 

                                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-edit-2" @click="popupActiveF(tr,indextr)"></vs-button>
                                  <vs-popup class="holamundo"  title="编辑数据上传通道" :active.sync="popupActive1" background-color="rgba(0,0,0,.1)">
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                     通道名称：
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                       <vs-input class="inputx" v-model="tmp_datach_title" />
                                    </vs-col> <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      <vs-button color="success" type="border" v-on:click="tmp_datach_update(tmp_datach_id)">更新</vs-button>
                                    </vs-col>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActive1=false">取消</vs-button>
                                    </vs-col>
                                   
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <!-- <vx-tooltip color="danger" text="删除"> -->
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="deldatachannel(tr.id)"> </vs-button>
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

            <vs-col >
              <vs-divider v-show="echartshow">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowline_no()" v-show="echartshow"> </vs-button>
              </vs-divider>

            <vs-row v-show="echartshow">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个数据点：</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入数值" v-model="measurement_test_value" /></vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_measurement_testvalue()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>
            <div id="echartContainer" style="width:100%; height:500px" v-show="echartshow"> </div>

            <vs-divider v-show="echartshow_dchswitch">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowline_no()" v-show="echartshow_dchswitch"> </vs-button>
              </vs-divider>

            <vs-row v-show="echartshow_dchswitch">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个开关状态：</vs-col>
                    <ul class="centerx">
                    <li>
                      <vs-radio color="success" v-model="switchstatus_test_value" vs-value="1">开</vs-radio>
                    </li>
                    <li>
                      <vs-radio color="danger" v-model="switchstatus_test_value" vs-value="0">关</vs-radio>
                    </li>
                  </ul>
                  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_switchstatus_testvalue()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>
            <div id="echartContainer_dchswitch" style="width:100%; height:500px" v-show="echartshow_dchswitch"> </div>
            
            <vs-divider v-show="echartshowmap">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmap_no()" v-if="echartshowmap"> </vs-button>
              </vs-divider>

              <vs-row v-show="echartshowmap">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">点击选择坐标</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">经度：{{lng_test_value}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">维度：{{lat_test_value}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3"><vs-input class="inputx" placeholder="输入地址" v-model="address_tmp" /></vs-col> 
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2"><vs-button color="success" type="filled" @click="input_position_testvalue()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>

            <baidu-map class="map" ak='2140eb7ba44386b17ef7f6601239b6b9' :center="center" :zoom="zoom"  @ready="handler" @click="getLocationPoint" style="width:100%;height:500px;" v-if="echartshowmap"  :scroll-wheel-zoom="true">
            </baidu-map>
            <vs-divider v-show="echartshowmsg">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmsg_no(tr)" v-show="echartshowmsg"> </vs-button>
              </vs-divider>

            <vs-row v-show="echartshowmsg">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一条消息：</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入消息" v-model="message_test_value" /></vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_message_testvalue()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>

            <VuePerfectScrollbar  :settings="settings" style="height:500px;" v-show="echartshowmsg">

              <ul class="activity-timeline" :key="indexmsg" v-for="(msg, indexmsg) in datamsg">
                <li>
                  <div class="timeline-icon bg-success">
                    <feather-icon icon="AlertCircleIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
                  </div>
                  <div class="timeline-info">
                    <span class="activity-desc">{{ msg.message }}</span>
                  </div>
                  <small class="text-grey activity-e-time">{{msg.timestamp | formatDate }}</small>
                </li>
          
               
              </ul>

        </VuePerfectScrollbar>
            
            </vs-col>
            
  
            </vx-card>
            </div>
            
        </div>
      </vs-tab>

      <vs-tab vs-label="双向通道" v-on:click="ctrlchannelinit()"> 
          <div class="flex flex-wrap">
            <div class="w-full sm:w-2/2 md:w-4/4">

             <vx-card class="overlay-card overflow-hidden">
              <vs-row>
                <vs-col>
                <h5><span class="text-success">双向控制通道：</span>控制点用于下发指令数据、上传状态数据。</h5>
                </vs-col>
              </vs-row>
            <br>
             <vs-row>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                <vs-input class="inputx" placeholder="通道名称" v-model="ctrlchannelName" />
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                <vs-select autocomplete class="selectExample" v-model="select2_datatype">
                  <vs-select-item :key="index" :value="item.value" :text="item.text" v-for="(item,index) in options2" />
                </vs-select>
              </vs-col>
              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                <vs-button color="success" type="border" v-on:click="addctrlchannel">添加</vs-button>
              </vs-col>
            </vs-row>
            <br>
            <vs-divider/>

            <vs-col>
              <vs-table :data="ctrlChanneltmp"  pagination max-items="5" >

                <template slot="thead">
                  <vs-th>通道名称</vs-th>
                  <vs-th>ID号</vs-th>
                  <vs-th>数据类型</vs-th>
                  <vs-th style="padding-left:20px;" >单位</vs-th> 
                  <vs-th >设备上传数据</vs-th> 
                  <vs-th >向设备下发数据</vs-th> 
                  <vs-th style="padding-left:60px;">操作</vs-th>
                </template>

                <template slot-scope="{data}">
                  <vs-tr :state="indextr == selectrow2 ? 'success':null"  :key="indextr" v-for="(tr, indextr) in data" >                   
   

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


                          <div v-if="tr.unitsymbol" style="margin-left:15px;">
                           {{ tr.unitsymbol }}
                           </div>  

                            <div v-else>
                           <span class="text-success"> 
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-plus"  @click="popupActiveF2ctrl(tr)"></vs-button>
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
                                            <vs-button class="mr-3 mb-2"  @click="addctrlunit(tmp_ctrlchid)">添加</vs-button>
                                            <vs-button color="warning" type="border" class="mb-2" @click="unitlabel=''; unitsymbol=''; unitstep=1;maxvalue=100;minvalue=1;">重置</vs-button>
                                          </div>
                                        </div>
                                      </vx-card>
                                    </div>
                                   
                                  </vs-popup>
                           </span>
                           </div> 
                           </div>
                          

                        <div v-else>
                          <span class="text-dark"> 
                                  <vs-button disabled  radius color="dark" type="flat" icon-pack="feather" icon="icon-minus"></vs-button>
                           </span>
                        </div>
                         
                      </vs-td>

                      <vs-td :data="data[indextr].datatype">

                      <div v-if="data[indextr].datatype === 'DECIMAL'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-bar-chart" @click="echartshowlinectrl(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'MESSAGE'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-message-circle" @click="echartshowmsgFunctrl(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'SWITCH'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-toggle-left" @click="echartshowswitchctrl(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else>
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-map-pin" @click="echartshowmapFunctrl(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>

                      </vs-td>

                      <vs-td :data="data[indextr].datatype">

                      <div v-if="data[indextr].datatype === 'DECIMAL'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-bar-chart" @click="echartshowlinectrl_down(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'MESSAGE'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-message-circle" @click="echartshowmsgFunctrl_down(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else-if="data[indextr].datatype === 'SWITCH'">
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-toggle-left" @click="echartshowswitchctrl_down(tr,indextr)"> </vs-button>
                                </vx-tooltip>
                        </span>
                      </div>
                      <div v-else>
                        <span class="text-success"> 
                                <vx-tooltip color="success" text="查看">
                                  <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-map-pin" @click="echartshowmapFunctrl_down(tr,indextr)"> </vs-button>
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
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                       <vs-input class="inputx" v-model="tmp_ctrlch_title" />
                                    </vs-col> <br>
                                    <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                      <vs-button color="success" type="border" v-on:click="tmp_ctrlch_update(tmp_ctrlch_id)">更新</vs-button>
                                    </vs-col>
                                   <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                     <vs-button color="warning" type="filled" @click="popupActive1ctrl=false">取消</vs-button>
                                    </vs-col>
                                  </vs-popup>
                                </vx-tooltip>
                              </span>
                              
                            </vs-col>
                            
                            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                              <span class="text-danger"> 
                                <!-- <vx-tooltip color="danger" text="删除"> -->
                                  <vs-button radius color="danger" type="flat" icon-pack="feather" icon="icon-trash" @click="delctrlchannel(tr.id)"> </vs-button>
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

            <vs-col>
                <vs-divider v-show="echartshowctrl">
                <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowlinectrl_no()" v-show="echartshowctrl"> </vs-button>
                </vs-divider>

                <vs-row v-show="echartshowctrl">
                <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                  <vx-card>
                    <vs-row>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个数据点：</vs-col>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入数值" v-model="metric_test_value" /></vs-col>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_metric_testvalue()">提交</vs-button></vs-col>
                    </vs-row>
                  </vx-card>
                </vs-col>
                <vs-divider/>
              </vs-row>

              <div id="echartContainerCtrl" style="width:100%; height:500px" v-show="echartshowctrl"> </div>

              <vs-divider v-show="echartshow_cchswitch">
              <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowlinectrl_no()" v-show="echartshow_cchswitch"> </vs-button>
                </vs-divider>

              <vs-row v-show="echartshow_cchswitch">
                <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                  <vx-card>
                    <vs-row>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个开关状态：</vs-col>
                      <ul class="centerx">
                      <li>
                        <vs-radio color="success" v-model="switchdata_test_value" vs-value="1">开</vs-radio>
                      </li>
                      <li>
                        <vs-radio color="danger" v-model="switchdata_test_value" vs-value="0">关</vs-radio>
                      </li>
                    </ul>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_switchdata_testvalue()">提交</vs-button></vs-col>
                    </vs-row>
                  </vx-card>
                </vs-col>
                <vs-divider/>
              </vs-row>
              <div id="echartContainerCtrl_cchswitch" style="width:100%; height:500px" v-show="echartshow_cchswitch"> </div>

              
              <vs-divider v-show="echartshowmapctrl">
              <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmapctrl_no()" v-if="echartshowmapctrl"> </vs-button>
                </vs-divider>

                <vs-row v-show="echartshowmapctrl">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">点击选择坐标</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">经度：{{lng_test_value_ctrl}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">维度：{{lat_test_value_ctrl}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3"><vs-input class="inputx" placeholder="输入地址" v-model="address_tmp_ctrl" /></vs-col> 
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2"><vs-button color="success" type="filled" @click="input_position_testvalue_ctrl()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>

              <baidu-map class="map" ak='2140eb7ba44386b17ef7f6601239b6b9' :center="center" :zoom="zoom"  @ready="handlerctrl" @click="getLocationPoint_ctrl" style="width:100%;height:500px;" v-if="echartshowmapctrl"  :scroll-wheel-zoom="true">
          
              </baidu-map>
              <vs-divider v-show="echartshowmsgctrl">
              <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmsgctrl_no(tr)" v-show="echartshowmsgctrl"> </vs-button>
                </vs-divider>

                <vs-row v-show="echartshowmsgctrl">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一条消息：</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入消息" v-model="message_test_value_ctrl" /></vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_message_testvalue_ctrl()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>

              <VuePerfectScrollbar  :settings="settings" style="height:500px;" v-show="echartshowmsgctrl">

                <ul class="activity-timeline" :key="indexmsg" v-for="(msg, indexmsg) in datamsgctrl">
                  <li>
                    <div class="timeline-icon bg-success">
                      <feather-icon icon="AlertCircleIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
                    </div>
                    <div class="timeline-info">
                      <span class="activity-desc">{{ msg.text }}</span>
                    </div>
                    <small class="text-grey activity-e-time">{{msg.timestamp | formatDate }}</small>
                  </li>
            
                
                </ul>

            </VuePerfectScrollbar>
          
          </vs-col>
             <vs-col>
              <vs-divider v-show="echartshowctrl_down">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowlinectrl_no_down()" v-show="echartshowctrl_down"> </vs-button>
              </vs-divider>

              <vs-row v-show="echartshowctrl_down">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个数据点：</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入数值" v-model="metric_test_value_down" /></vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_metric_testvalue_down()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>
            <div id="echartContainerCtrl_down" style="width:100%; height:500px" v-show="echartshowctrl_down"> </div>

            <vs-row v-show="echartshow_cchswitch_down">
                <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                  <vx-card>
                    <vs-row>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一个开关状态：</vs-col>
                      <ul class="centerx">
                      <li>
                        <vs-radio color="success" v-model="switchdata_test_value_down" vs-value="1">开</vs-radio>
                      </li>
                      <li>
                        <vs-radio color="danger" v-model="switchdata_test_value_down" vs-value="0">关</vs-radio>
                      </li>
                    </ul>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_switchdata_testvalue_down()">提交</vs-button></vs-col>
                    </vs-row>
                  </vx-card>
                </vs-col>
                <vs-divider/>
              </vs-row>
              <div id="echartContainerCtrl_cchswitch_down" style="width:100%; height:500px" v-show="echartshow_cchswitch_down"> </div>
            
            <vs-divider v-show="echartshowmapctrl_down">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmapctrl_no_down()" v-if="echartshowmapctrl_down"> </vs-button>
              </vs-divider>

             <vs-row v-show="echartshowmapctrl_down">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">点击选择坐标</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">经度：{{lng_test_value_ctrl_down}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">维度：{{lat_test_value_ctrl_down}}</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3"><vs-input class="inputx" placeholder="输入地址" v-model="address_tmp_ctrl_down" /></vs-col> 
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2"><vs-button color="success" type="filled" @click="input_position_testvalue_ctrl_down()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>

            <baidu-map class="map" ak='2140eb7ba44386b17ef7f6601239b6b9' :center="center" :zoom="zoom"  @ready="handlerctrl_down" @click="getLocationPoint_ctrl_down"  style="width:100%;height:500px;" v-if="echartshowmapctrl_down"  :scroll-wheel-zoom="true">
         
            </baidu-map>
            <vs-divider v-show="echartshowmsgctrl_down">
            <vs-button radius color="success" type="flat" icon-pack="feather" icon="icon-camera-off" @click="echartshowmsgctrl_no_down(tr)" v-show="echartshowmsgctrl_down"> </vs-button>
              </vs-divider>

              <vs-row v-show="echartshowmsgctrl_down">
              <vs-col vs-offset="1" v-tooltip="'col - 10'" vs-type="flex" vs-justify="center" vs-align="center" vs-w="10">
                <vx-card>
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4">输入一条消息：</vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-input class="inputx" placeholder="输入消息" v-model="message_test_value_ctrl_down" /></vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="4"><vs-button color="success" type="filled" @click="input_message_testvalue_ctrl_down()">提交</vs-button></vs-col>
                  </vs-row>
                </vx-card>
              </vs-col>
              <vs-divider/>
            </vs-row>
            <VuePerfectScrollbar  :settings="settings" style="height:500px;" v-show="echartshowmsgctrl_down">

              <ul class="activity-timeline" :key="indexmsg" v-for="(msg, indexmsg) in datamsgctrl_down">
                <li>
                  <div class="timeline-icon bg-success">
                    <feather-icon icon="AlertCircleIcon" svgClasses="text-white stroke-current w-5 h-5"></feather-icon>
                  </div>
                  <div class="timeline-info">
                    <span class="activity-desc">{{ msg.text }}</span>
                  </div>
                  <small class="text-grey activity-e-time">{{msg.timestamp | formatDate }}</small>
                </li>
          
               
              </ul>

        </VuePerfectScrollbar>
            
            </vs-col>

            </vx-card>


            
            </div>
            
        </div>
      </vs-tab>

      <!-- <vs-tab vs-label="时间计划" @click="init_schedule()"> 
          <div> <br> </div>
          <div class="flex flex-wrap">
            <vs-tabs vs-alignment="fixed">
            <vs-tab vs-label="间隔时间" style="width:100%;">
              <div style="width:100%">
                <vs-row vs-justify="center">
                  <vs-col type="flex" vs-justify="center" vs-align="center" vs-w="12">
                    <vs-card>
                      <div>
                        <p><br></p>
                      </div>
                      <vs-row>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
                          <div class="centerx">
                            <span>间隔：</span>
                          </div>
                        </vs-col>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="3">
                          <vs-input-number color="success" min="1" v-model="interval_num" />
                        </vs-col>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
                          <div class="centerx">
                            <span>周期：</span>
                          </div>
                        </vs-col>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                          <vs-select autocomplete class="selectExample" v-model="select_interval">
                            <vs-select-item
                              :key="index"
                              :value="item.value"
                              :text="item.text"
                              v-for="(item,index) in options_interval"
                            />
                          </vs-select>
                        </vs-col>

                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                          <vs-button
                            color="success"
                            type="flat"
                            icon-pack="feather"
                            icon="icon-plus"
                            v-on:click="addinterval()"
                          >添加间隔时间</vs-button>
                        </vs-col>
                      </vs-row>
                      <vs-row><vs-divider/></vs-row>
                      <vs-table max-items="10" pagination :data="intervalList">
                        <template slot="thead">
                          <vs-th>ID号</vs-th>
                          <vs-th>间隔</vs-th>
                          <vs-th>周期</vs-th>
                          <vs-th>描述</vs-th>
                          <div style="padding-left:15%;">
                            <vs-th>操作</vs-th>
                          </div>
                        </template>

                        <template slot-scope="{data}">
                          <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                            <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                            <vs-td :data="data[indextag].every">{{ data[indextag].every}}</vs-td>

                            <vs-td :data="data[indextag].period">{{ data[indextag].period }}</vs-td>
                            <vs-td
                              :data="data[indextag].period"
                            >每隔{{ data[indextag].every}}{{ data[indextag].period }}</vs-td>
                            <vs-td>
                              <vs-row>
                                <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                  <span class="text-success">
                                    <vx-tooltip color="primary" text="编辑">
                                      <vs-button
                                        radius
                                        color="success"
                                        type="flat"
                                        icon-pack="feather"
                                        icon="icon-edit-2"
                                        @click="popupActiveInterval_updatefunc(tag)"
                                      ></vs-button>
                                      <vs-popup
                                        class="holamundo"
                                        title="编辑间隔时间"
                                        :active.sync="popupActiveInterval_update"
                                        background-color="rgba(0,0,0,.1)"
                                      >
                                        <vs-row vs-type="flex" vs-w="12">间隔：</vs-row>
                                        <vs-row vs-type="flex" vs-w="12">
                                          <vs-input class="inputx w-full" v-model="interval_every" />
                                        </vs-row>
                                        <vs-row vs-type="flex" vs-w="12">周期：</vs-row>
                                        <vs-row vs-type="flex" vs-w="12">
                                          <v-select
                                            class="vx-col w-full"
                                            label="select1_period"
                                            :options="['DAYS','HOURS','MINUTES','SECONDS','MICROSECONDS']"
                                            v-model="select1_period"
                                          ></v-select>
                                        </vs-row>
                                        <vs-row>
                                          <br />
                                        </vs-row>

                                        <vs-row v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="success"
                                              type="border"
                                              @click="interval_update(tmp_interval_id)"
                                            >更新</vs-button>
                                          </vs-col>
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="warning"
                                              type="filled"
                                              @click="popupActiveInterval_update=false"
                                            >取消</vs-button>
                                          </vs-col>
                                        </vs-row>
                                        <vs-row>
                                          <br />
                                          <br />
                                          <br />
                                          <br />
                                          <br />
                                        </vs-row>
                                      </vs-popup>
                                    </vx-tooltip>
                                  </span>
                                </vs-col>

                                <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                  <span class="text-danger">
                                    <vx-tooltip color="danger" text="删除">
                                      <vs-button
                                        radius
                                        color="danger"
                                        type="flat"
                                        icon-pack="feather"
                                        icon="icon-trash"
                                        @click="popupActiveInterval_delfunc(tag)"
                                      ></vs-button>
                                      <vs-popup
                                        class="holamundo"
                                        title="删除间隔时间"
                                        :active.sync="popupActiveInterval_del"
                                        background-color="rgba(0,0,0,.1)"
                                      >
                                        <vs-row vs-justify="center">
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="danger"
                                              type="filled"
                                              @click="delinterval(tmp_interval_id)"
                                            >确认删除</vs-button>
                                          </vs-col>
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="warning"
                                              type="filled"
                                              @click="popupActiveInterval_del=false"
                                            >取消</vs-button>
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
 
                    </vs-card>
                  </vs-col>
                </vs-row>
              </div>

            </vs-tab>
            <vs-tab vs-label="定时时间" @click="clockedinit()">
            <div>
              <div class="flex flex-wrap">
                <vs-row>
                  <vs-col
                    vs-offset="0"
                    v-tooltip="'col - 8'"
                    vs-type="flex"
                    vs-justify="center"
                    vs-align="center"
                    vs-w="12"
                  >
                    <vx-card class="overlay-card overflow-hidden">
                      <vs-row>
                        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                          <div class="centerx">
                            <span>定时：</span>
                          </div>
                        </vs-col>
                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="4">
                          <flat-pickr
                            :config="configs.dateTimePicker"
                            id="datetime-input"
                            class="form-control"
                            v-model="form.dateTime"
                            placeholder="选择时间"
                            style="height:40px;width:300px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                          ></flat-pickr>
                        </vs-col>

                        <vs-col
                          vs-type="flex"
                          vs-justify="center"
                          vs-align="center"
                          vs-w="2"
                          style="padding-bottom:2px;"
                        >
                          <feather-icon icon="PlayCircleIcon" svgClasses="text-grey"></feather-icon>
                          <span style="padding-left:10px;">启用</span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                          <vs-button
                            color="success"
                            type="flat"
                            icon-pack="feather"
                            icon="icon-plus"
                            v-on:click="addclocked()"
                          >添加定时时间</vs-button>
                        </vs-col>
                      </vs-row>
                      <vs-divider />
                      <br />
                      <vs-table max-items="10" pagination :data="clockedList">
                        <template slot="thead">
                          <vs-th>ID号</vs-th>
                          <vs-th>定时</vs-th>
                          <vs-th>启用</vs-th>
                          <div style="padding-left:15%;">
                            <vs-th>操作</vs-th>
                          </div>
                        </template>

                        <template slot-scope="{data}">
                          <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                            <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                            <vs-td
                              :data="data[indextag].clocked_time"
                            >{{ data[indextag].clocked_time | formatDate}}</vs-td>

                            <vs-td :data="data[indextag].enabled">{{ data[indextag].enabled }}</vs-td>

                            <vs-td>
                              <vs-row>
                                <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                  <span class="text-success">
                                    <vx-tooltip color="primary" text="编辑">
                                      <vs-button
                                        radius
                                        color="success"
                                        type="flat"
                                        icon-pack="feather"
                                        icon="icon-edit-2"
                                        @click="popupActiveClocked_updatefunc(tag)"
                                      ></vs-button>
                                      <vs-popup
                                        class="holamundo"
                                        title="编辑定时时间"
                                        :active.sync="popupActiveClocked_update"
                                        background-color="rgba(0,0,0,.1)"
                                      >
                                        <vs-row vs-type="flex" vs-w="12">
                                          <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                            <flat-pickr
                                              :config="configs.dateTimePicker"
                                              id="datetime-input"
                                              class="form-control"
                                              v-model="form.dateTime"
                                              placeholder="选择时间"
                                              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                                            ></flat-pickr>
                                          </vs-col>
                                        </vs-row>
                                        <vs-row>
                                          <br />
                                          <br />
                                        </vs-row>

                                        <vs-row v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                            <vs-button
                                              color="success"
                                              type="border"
                                              @click="Clocked_update(tmp_clocked_id)"
                                            >更新</vs-button>
                                          </vs-col>

                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="6">
                                            <vs-button
                                              color="warning"
                                              type="filled"
                                              @click="popupActiveClocked_update=false"
                                            >取消</vs-button>
                                          </vs-col>
                                        </vs-row>
                                      </vs-popup>
                                    </vx-tooltip>
                                  </span>
                                </vs-col>

                                <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                  <span class="text-danger">
                                    <vx-tooltip color="danger" text="删除">
                                      <vs-button
                                        radius
                                        color="danger"
                                        type="flat"
                                        icon-pack="feather"
                                        icon="icon-trash"
                                        @click="popupActiveClocked_delfunc(tag)"
                                      ></vs-button>
                                      <vs-popup
                                        class="holamundo"
                                        title="删除定时时间"
                                        :active.sync="popupActiveClocked_del"
                                        background-color="rgba(0,0,0,.1)"
                                      >
                                        <vs-row vs-justify="center">
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="danger"
                                              type="filled"
                                              @click="delclocked(tmp_clocked_id)"
                                            >确认删除</vs-button>
                                          </vs-col>
                                          <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                            <vs-button
                                              color="warning"
                                              type="filled"
                                              @click="popupActiveClocked_del=false"
                                            >取消</vs-button>
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
          <vs-tab vs-label="例行时间" @click="cronsinit()">
          <div>
            <div class="flex flex-wrap">
              <vs-row>
                <vs-col
                  vs-offset="0"
                  v-tooltip="'col - 8'"
                  vs-type="flex"
                  vs-justify="center"
                  vs-align="center"
                  vs-w="12"
                >
                  <vx-card class="overlay-card overflow-hidden">
                    <vs-row>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                        <div class="centerx">
                          <span>分钟：</span>
                        </div>
                      </vs-col>
                      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                        <vs-input v-model="crons_minute" class="w-full" />
                      </vs-col>
                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                        <div class="centerx">
                          <span>小时：</span>
                        </div>
                      </vs-col>
                      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                        <vs-input v-model="crons_hour" class="w-full" />
                      </vs-col>

                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                        <div class="centerx">
                          <span>天/周：</span>
                        </div>
                      </vs-col>
                      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                        <vs-input v-model="crons_weekday" class="w-full" />
                      </vs-col>

                      <vs-row>
                        <br />
                      </vs-row>

                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                        <div class="centerx">
                          <span>天/月：</span>
                        </div>
                      </vs-col>
                      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                        <vs-input v-model="crons_monthday" class="w-full" />
                      </vs-col>

                      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="2">
                        <div class="centerx">
                          <span>月/年：</span>
                        </div>
                      </vs-col>
                      <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                        <vs-input v-model="crons_yearmonth" class="w-full" />
                      </vs-col>

                      <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-plus"
                          v-on:click="addcrons()"
                        >添加例行时间</vs-button>
                      </vs-col>
                    </vs-row>
                    <vs-divider />
                    <br />
                    <vs-table max-items="10" pagination :data="cronsList">
                      <template slot="thead">
                        <vs-th>ID号</vs-th>
                        <vs-th>名称</vs-th>
                        <vs-th>例行月</vs-th>
                        <vs-th>天(月)</vs-th>
                        <vs-th>天(周)</vs-th>
                        <vs-th>小时</vs-th>
                        <vs-th>分钟</vs-th>
                        <div style="padding-left:15%;">
                          <vs-th>操作</vs-th>
                        </div>
                      </template>

                      <template slot-scope="{data}">
                        <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                          <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                          <vs-td
                            :data="data[indextag].id"
                          >每年的第{{ data[indextag].month_of_year }}月-每月的第{{ data[indextag].day_of_month }}天-每周的第{{ data[indextag].day_of_week }}天-第{{ data[indextag].hour }}个小时-第{{ data[indextag].minute }}分钟</vs-td>

                          <vs-td
                            :data="data[indextag].month_of_year"
                          >{{ data[indextag].month_of_year }}</vs-td>

                          <vs-td :data="data[indextag].day_of_month">{{ data[indextag].day_of_month }}</vs-td>

                          <vs-td :data="data[indextag].day_of_week">{{ data[indextag].day_of_week }}</vs-td>

                          <vs-td :data="data[indextag].hour">{{ data[indextag].hour }}</vs-td>

                          <vs-td :data="data[indextag].minute">{{ data[indextag].minute }}</vs-td>

                          <vs-td>
                            <vs-row>
                              <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="编辑">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-edit-2"
                                      @click="popupActiveCrons_updatefunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="编辑例行时间"
                                      :active.sync="popupActiveCrons_update"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-type="flex" vs-w="12">
                                        <vs-col
                                          vs-type="flex"
                                          vs-justify="center"
                                          vs-align="center"
                                          vs-w="2"
                                        >
                                          <div class="centerx">
                                            <span>分钟：</span>
                                          </div>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                          <vs-input v-model="crons_minute_input" class="w-full" />
                                        </vs-col>
                                        <vs-col
                                          vs-type="flex"
                                          vs-justify="center"
                                          vs-align="center"
                                          vs-w="2"
                                        >
                                          <div class="centerx">
                                            <span>小时：</span>
                                          </div>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                          <vs-input v-model="crons_hour_input" class="w-full" />
                                        </vs-col>

                                        <vs-col
                                          vs-type="flex"
                                          vs-justify="center"
                                          vs-align="center"
                                          vs-w="2"
                                        >
                                          <div class="centerx">
                                            <span>天/周：</span>
                                          </div>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                          <vs-input v-model="crons_weekday_input" class="w-full" />
                                        </vs-col>

                                        <vs-row>
                                          <br />
                                        </vs-row>

                                        <vs-col
                                          vs-type="flex"
                                          vs-justify="center"
                                          vs-align="center"
                                          vs-w="2"
                                        >
                                          <div class="centerx">
                                            <span>天/月：</span>
                                          </div>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                          <vs-input v-model="crons_monthday_input" class="w-full" />
                                        </vs-col>

                                        <vs-col
                                          vs-type="flex"
                                          vs-justify="center"
                                          vs-align="center"
                                          vs-w="2"
                                        >
                                          <div class="centerx">
                                            <span>月/年：</span>
                                          </div>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                          <vs-input v-model="crons_yearmonth_input" class="w-full" />
                                        </vs-col>
                                      </vs-row>
                                      <vs-row>
                                        <br />
                                        <br />
                                      </vs-row>

                                      <vs-row v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="success"
                                            type="border"
                                            @click="Crons_update(tmp_crons_id)"
                                          >更新</vs-button>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveCrons_update=false"
                                          >取消</vs-button>
                                        </vs-col>
                                      </vs-row>
                                    </vs-popup>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 1'" vs-type="flex" vs-w="2">
                                <span class="text-danger">
                                  <vx-tooltip color="danger" text="删除">
                                    <vs-button
                                      radius
                                      color="danger"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-trash"
                                      @click="popupActiveCrons_delfunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="删除例行时间"
                                      :active.sync="popupActiveCrons_del"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-justify="center">
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="danger"
                                            type="filled"
                                            @click="delcrons(tmp_crons_id)"
                                          >确认删除</vs-button>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveCrons_del=false"
                                          >取消</vs-button>
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
      </vs-tab>

      <vs-tab vs-label="执行动作" @click="init_httpaction()"> 
           
          <div class="flex flex-wrap">
            <vs-tabs vs-alignment="fixed">
            <vs-tab vs-label="HTTP动作">
               <vs-row>
                <div class="w-3/4">              
                  <vx-card class="overlay-card overflow-hidden">
                    <vs-row>
                      <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="2">
                        <vs-input class="inputx w-full" placeholder="动作名称" v-model="globalact_title" />
                      </vs-col>
                      <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="6">
                        <vs-input class="inputx w-full" placeholder="动作URL" v-model="globalact_url" />
                      </vs-col>
                      <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-plus"
                          v-on:click="addglobalhttpaction()"
                        >添加HTTP动作</vs-button>
                      </vs-col>
                    </vs-row>
                    <br />
                    <vs-divider />
                    <br />
                    <vs-table max-items="10" pagination :data="globalhttpactionList">
                      <template slot="thead">
                        <vs-th>ID</vs-th>
                        <vs-th>动作名称</vs-th>
                        <vs-th>动作URL</vs-th>
                        <vs-th style="padding-left:60px;">操作</vs-th>
                      </template>

                      <template slot-scope="{data}">
                        <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                          <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                          <vs-td :data="data[indextag].title">{{ data[indextag].title }}</vs-td>

                          <vs-td :data="data[indextag].url">{{ data[indextag].url }}</vs-td>
                          <vs-td style="width:200px;">
                            <vs-row>
                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="参数管理">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-file-text"
                                      v-on:click="show_actionparams(tag)"
                                    ></vs-button>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="编辑">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-edit-2"
                                      @click="popupActiveHttpact_updatefunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="编辑HTT动作"
                                      :active.sync="popupActiveHttpact_update"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">动作名称：</vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-input class="inputx" v-model="globalhttpaction_title_tmp" />
                                      </vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">动作URL：</vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-textarea class="inputx" v-model="globalhttpaction_url_tmp" />
                                      </vs-col>
                                      <br />
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-button
                                          color="success"
                                          type="border"
                                          @click="globalhttpaction_update(globalhttpaction_id_tmp)"
                                        >更新</vs-button>
                                      </vs-col>
                                    </vs-popup>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-danger">
                                  <vx-tooltip color="danger" text="删除">
                                    <vs-button
                                      radius
                                      color="danger"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-trash"
                                      @click="popupActiveHttpact_delfunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="删除HTTP动作"
                                      :active.sync="popupActiveHttpact_del"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-justify="center">
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="danger"
                                            type="filled"
                                            @click="delglobalhttpact(globalhttpaction_id_tmp)"
                                          >确认删除</vs-button>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveHttpact_del=false"
                                          >取消</vs-button>
                                        </vs-col>
                                      </vs-row>
                                    </vs-popup>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="测试HTTP动作状态">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-refresh-ccw"
                                      v-on:click="test_actionstatus(tag)"
                                    ></vs-button>
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

                <div class="w-1/4" v-show="!showactionparams" style="padding-left:20px;">
                <p>注：添加参数时需要注意，需要根据HTTP接口的要求定义请求的参数</p>
                </div>

                <div class="w-full sm:w-1/2 md:w-1/4 px-2" v-show="showactionparams" > 
                  <vx-card class="overlay-card overflow-hidden">
                    <h6>所属动作名称：{{ globalhttpaction_title }}</h6>
                    <vs-divider />
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-input class="inputx" placeholder="参数key" v-model="httpactparamKey" />
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-input class="inputx" placeholder="参数value" v-model="httpactparamValue" />
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-button
                        color="success"
                        type="border"
                        v-on:click="addhttpactparam(globalhttpaction_id)"
                      >添加</vs-button>
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>

                    <vs-divider>参数列表</vs-divider>
                  
                    <vs-table max-items="5" pagination :data="httpactparamList" >
                      <template slot="thead">
                        <vs-th>ID</vs-th>
                        <vs-th>KEY</vs-th>
                        <vs-th>VALUE</vs-th>
                        <vs-th style="padding-left:40px;">操作</vs-th>
                      </template>

                      <template slot-scope="{data}">
                        <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                          <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>
                          <vs-td :data="data[indextr].key">{{ data[indextr].key }}</vs-td>

                          <vs-td :data="data[indextr].value">{{ data[indextr].value }}</vs-td>

                          <vs-td>
                            <vs-row>
                              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                                <span class="text-danger">
                                  <vx-tooltip color="danger" text="删除">
                                    <vs-button
                                      radius
                                      color="danger"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-trash"
                                      @click="popupActiveActparam_func(tr)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="删除动作参数"
                                      :active.sync="popupActiveActparam_del"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-justify="center">
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="danger"
                                            type="filled"
                                            @click="delactparam(httpactparam_id)"
                                          >确认删除</vs-button>
                                        </vs-col>

                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveActparam_del=false"
                                          >取消</vs-button>
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
                </div>
              </vs-row>
            </vs-tab>
            <vs-tab vs-label="MQTT动作"  @click="init_mqtt_action()">
               <vs-row>
                <div class="w-3/4">
                  <vx-card class="overlay-card overflow-hidden">
                    <br />
                    <vs-row>
                      <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="2">
                        <vs-input
                          class="inputx w-full"
                          placeholder="动作名称"
                          v-model="global_mqtt_act_title"
                        />
                      </vs-col>
                      <vs-col v-tooltip="'col - 8'" vs-type="flex" vs-w="6">
                        <vs-input
                          class="inputx w-full"
                          placeholder="主题topic"
                          v-model="global_mqtt_topic"
                        />
                      </vs-col>
                      <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="success"
                          type="flat"
                          icon-pack="feather"
                          icon="icon-plus"
                          v-on:click="addglobalmqttaction()"
                        >添加MQTT动作</vs-button>
                      </vs-col>
                    </vs-row>
                    <br />
                    <vs-divider />
                    <br />
                    <vs-table max-items="10" pagination :data="globalmqttactionList">
                      <template slot="thead">
                        <vs-th>ID</vs-th>
                        <vs-th>MQTT动作名称</vs-th>
                        <vs-th>MQTT Topic</vs-th>
                        <vs-th style="padding-left:60px;">操作</vs-th>
                      </template>

                      <template slot-scope="{data}">
                        <vs-tr :key="indextag" v-for="(tag, indextag) in data">
                          <vs-td :data="data[indextag].id">{{ data[indextag].id }}</vs-td>

                          <vs-td :data="data[indextag].title">{{ data[indextag].title }}</vs-td>

                          <vs-td :data="data[indextag].topic">{{ data[indextag].topic }}</vs-td>
                          <vs-td style="width:200px;">
                            <vs-row>
                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="参数管理">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-file-text"
                                      v-on:click="show_mqttactionparams(tag)"
                                    ></vs-button>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-success">
                                  <vx-tooltip color="primary" text="编辑">
                                    <vs-button
                                      radius
                                      color="success"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-edit-2"
                                      @click="popupActiveMqttact_updatefunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="编辑MQTT动作"
                                      :active.sync="popupActiveMqttact_update"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">MQTT动作名称：</vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-input class="inputx" v-model="globalmqttaction_title_tmp" />
                                      </vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">MQTT Topic：</vs-col>
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-textarea class="inputx" v-model="globalmqttaction_topic_tmp" />
                                      </vs-col>
                                      <br />
                                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="12">
                                        <vs-button
                                          color="success"
                                          type="border"
                                          @click="globalmqttaction_update(globalmqttaction_id_tmp)"
                                        >更新</vs-button>
                                      </vs-col>
                                    </vs-popup>
                                  </vx-tooltip>
                                </span>
                              </vs-col>

                              <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                                <span class="text-danger">
                                  <vx-tooltip color="danger" text="删除">
                                    <vs-button
                                      radius
                                      color="danger"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-trash"
                                      @click="popupActiveMqttpact_delfunc(tag)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="删除MQTT动作"
                                      :active.sync="popupActiveMqttact_del"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-justify="center">
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="danger"
                                            type="filled"
                                            @click="delglobalmqttact(globalmqttaction_id_tmp)"
                                          >确认删除</vs-button>
                                        </vs-col>
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveMqttact_del=false"
                                          >取消</vs-button>
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
                </div>
                <div class="w-1/4" v-show="!showmqttactionparams" style="padding-left:20px;">
                 <p>注：添加参数时需要注意，需要根据MQTT的要求定义请求的参数</p>
                </div>
                <div class="w-full sm:w-1/2 md:w-1/4 px-2" v-show="showmqttactionparams">
                  <vx-card class="overlay-card overflow-hidden">
                    <h6>所属动作名称：{{ globalmqttaction_title }}</h6>
                    <vs-divider />
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-input class="inputx" placeholder="参数key" v-model="mqttactparamKey" />
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-input class="inputx" placeholder="参数value" v-model="mqttactparamValue" />
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>
                    <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="12">
                      <vs-button
                        color="success"
                        type="border"
                        v-on:click="addmqttactparam(globalmqttaction_id)"
                      >添加</vs-button>
                    </vs-col>
                    <vs-row>
                      <br />
                    </vs-row>

                    <vs-divider>参数列表</vs-divider>

                    <vs-table max-items="5" pagination :data="mqttactparamList">
                      <template slot="thead">
                        <vs-th>ID</vs-th>
                        <vs-th>KEY</vs-th>
                        <vs-th>VALUE</vs-th>
                        <vs-th style="padding-left:40px;">操作</vs-th>
                      </template>

                      <template slot-scope="{data}">
                        <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data" >
                          <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>
                          <vs-td :data="data[indextr].key">{{ data[indextr].key }}</vs-td>

                          <vs-td :data="data[indextr].value">{{ data[indextr].value }}</vs-td>

                          <vs-td>
                            <vs-row>
                              <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                                <span class="text-danger">
                                  <vx-tooltip color="danger" text="删除">
                                    <vs-button
                                      radius
                                      color="danger"
                                      type="flat"
                                      icon-pack="feather"
                                      icon="icon-trash"
                                      @click="popupActiveMqttActparam_func(tr)"
                                    ></vs-button>
                                    <vs-popup
                                      class="holamundo"
                                      title="删除动作参数"
                                      :active.sync="popupActiveMqttActparam_del"
                                      background-color="rgba(0,0,0,.1)"
                                    >
                                      <vs-row vs-justify="center">
                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="danger"
                                            type="filled"
                                            @click="delmqttactparam(mqttactparam_id)"
                                          >确认删除</vs-button>
                                        </vs-col>

                                        <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                          <vs-button
                                            color="warning"
                                            type="filled"
                                            @click="popupActiveMqttActparam_del=false"
                                          >取消</vs-button>
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
                </div>
              </vs-row>
            </vs-tab>

          </vs-tabs>
          </div>
      </vs-tab>

      <vs-tab vs-label="计划任务" @click="initschedulejob()"> 
           <vs-row>
      <vs-col vs-type="flex" vs-justify="left" vs-align="center" vs-w="4">
        <vs-button color="success" type="filled" @click="popupActive_schedulejobcreate()">新增时间计划任务</vs-button>
      </vs-col>

      <vs-popup title="创建一个新的计划任务" :active.sync="popupActive_schedulejob">
        <div class="vx-row">
          <div class="vx-col w-full">
            <p>
              任务名称
              <font color="#FF0000">*</font>
            </p>
            <vs-input v-model="task_title" class="w-full" />
            <br />
          </div>
          <div class="vx-col w-full">
            <p>任务描述</p>
            <vs-textarea v-model="task_description" class="w-full" />
          </div>
          <div class="vx-col w-full">
            <p>
              时间计划类型
              <font color="#FF0000">*</font>
            </p>
            <v-select
              autocomplete
              :options="['INTERVAL','CRONS','CLOCKED']"
              v-model="schedule_type"
              :input-changed="showscheduleinput()"
            ></v-select>
            <br />
          </div>
          <div class="vx-col w-full" v-show="schedule_interval_input">
            <p>选择间隔时间</p>
            <select
              autocomplete
              placeholder="选择间隔时间"
              class="selectExample w-full"
              v-model="select1_interval"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            >
              <option
                :key="index"
                :value="item.id"
                v-for="(item,index) in options1_interval"
              >每隔{{ item.every }}{{ item.period }}</option>
            </select>
          </div>
          <div class="vx-col w-full" v-show="schedule_cron_input">
            <p>选择例行时间</p>
            <select
              autocomplete
              placeholder="选择例行时间"
              class="selectExample w-full"
              v-model="select1_cron"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            >
              <option
                :key="index"
                :value="item.id"
                v-for="(item,index) in options1_cron"
              >分钟-时-天/周-天/月-月/年{{ item.minute }} {{ item.hour }} {{ item.day_of_week }} {{ item.day_of_month }} {{ item.month_of_year }}</option>
            </select>
          </div>
          <div class="vx-col w-full" v-show="schedule_clocked_input">
            <p>选择定时时间</p>
            <select
              autocomplete
              placeholder="选择定时时间"
              class="selectExample w-full"
              v-model="select1_clocked"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            >
              <option
                :key="index"
                :value="item.id"
                v-for="(item,index) in options1_clocked"
              >{{ item.clocked_time | formatDate }}</option>
            </select>
          </div>
          <div class="vx-col w-full">
            <p>任务开始时间</p>
            <flat-pickr
              :config="configsjob.dateTimePickerJob"
              id="datetime-input"
              class="form-control"
              v-model="formjob.startdateTimeJob"
              placeholder="选择时间"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            ></flat-pickr>
            <br />
          </div>
          <div class="vx-col w-full">
            <br />
            <p>任务结束时间</p>
            <flat-pickr
              :config="configsjob.dateTimePickerJob"
              id="datetime-input"
              class="form-control"
              v-model="formjob.enddateTimeJob"
              placeholder="选择时间"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            ></flat-pickr>
          </div>
          <div class="vx-col w-full">
            <br />
            <p>任务运行状态</p>
          </div>
          <div class="vx-col w-full">
            <ul class="centerx">
              <li>
                <vs-radio
                  class="vx-col w-1/4 mt-4"
                  color="success"
                  v-model="task_enabled"
                  vs-value="True"
                >True</vs-radio>
                <vs-radio
                  class="vx-col w-1/4 mt-4"
                  color="danger"
                  v-model="task_enabled"
                  vs-value="False"
                >False</vs-radio>
              </li>
            </ul>
          </div>
          <div class="vx-col w-full">
            <p>
              选择动作类型
              <font color="#FF0000">*</font>
            </p>
            <v-select
              autocomplete
              :options="['HTTP','MQTT']"
              v-model="schedule_action_type"
              :input-changed="showschedule_actioninput()"
            ></v-select>
            <br />
          </div>
          <div class="vx-col w-full" v-show="schedule_httpaction_input">
            <p>
              选择HTTP执行动作
              <font color="#FF0000">*</font>
            </p>
            <select
              autocomplete
              placeholder="选择HTTP动作"
              class="selectExample w-full"
              v-model="select1_action"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            >
              <option
                :key="index"
                :value="item.id"
                v-for="(item,index) in options1_action"
              >{{item.title}}</option>
            </select>
          </div>
          <div class="vx-col w-full" v-show="schedule_mqttaction_input">
            <p>
              选择MQTT执行动作
              <font color="#FF0000">*</font>
            </p>
            <select
              autocomplete
              placeholder="选择MQTT动作"
              class="selectExample w-full"
              v-model="select2_action"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            >
              <option
                :key="index"
                :value="item.id"
                v-for="(item,index) in options2_action"
              >{{item.title}}</option>
            </select>
          </div>
          <div class="vx-col w-full">
            <vs-button
              class="vx-col w-1/3 mt-3"
              type="border"
              color="success"
              v-on:click="addschedulejob()"
            >添加计划任务</vs-button>
          </div>
        </div>
      </vs-popup>

      <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
        <vs-input
          placeholder="搜索计划任务"
          v-model="knowledgeBaseSearchQuery"
          icon-pack="feather"
          icon="icon-search"
          class="w-full no-icon-border mt-4"
        />
      </vs-col>
    </vs-row>

    <vs-divider />

    <vs-table pagination max-items="10" :data="filteredKB" stripe>
      <template slot="thead">
        <vs-th>序号</vs-th>
        <vs-th>任务名称</vs-th>
        <vs-th>时间计划</vs-th>
        <vs-th>开始时间</vs-th>
        <vs-th>结束时间</vs-th>
        <vs-th>动作名称</vs-th>
        <vs-th>状态</vs-th>

        <vs-th style="padding-left:60px;">操作</vs-th>
      </template>

      <template slot-scope="{data}">
        <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
          <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>

          <vs-td :data="data[indextr].name">{{ data[indextr].name }}</vs-td>

          <vs-td :data="data[indextr].scheduleplan">{{ data[indextr].scheduleplan }}</vs-td>

          <vs-td :data="data[indextr].start_time">{{ data[indextr].start_time | formatDate }}</vs-td>

          <vs-td :data="data[indextr].expires">{{ data[indextr].expires | formatDate }}</vs-td>

          <vs-td :data="data[indextr].action">{{ data[indextr].action }}</vs-td>

          <vs-td :data="data[indextr].enabled">
            <span class="text-success" v-if="data[indextr].enabled==true">运行</span>
            <span class="text-warning" v-else>停止</span>
          </vs-td>

          <vs-td>
            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-if="tr.enabled==false">
              <span class="text-danger">
                <vx-tooltip color="success" text="启动任务">
                  <vs-button
                    radius
                    color="success"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-play"
                    @click="schedulejob_start(tr,indextr)"
                  ></vs-button>
                </vx-tooltip>
              </span>
            </vs-col>
            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-else>
              <span class="text-danger">
                <vx-tooltip color="warning" text="停止任务">
                  <vs-button
                    radius
                    color="warning"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-pause"
                    @click="schedulejob_stop(tr,indextr)"
                  ></vs-button>
                </vx-tooltip>
              </span>
            </vs-col>

            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
              <span class="text-danger">
                <vx-tooltip color="danger" text="删除">
                  <vs-button
                    radius
                    color="danger"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-trash"
                    @click="popupActiveScheduleJob_delfunc(tr)"
                  ></vs-button>

                  <vs-popup
                    class="holamundo"
                    title="删除计划任务"
                    :active.sync="popupActiveScheduleJob_del"
                    background-color="rgba(0,0,0,.1)"
                  >
                    <vs-row vs-justify="center">
                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="danger"
                          type="filled"
                          @click="delete_schedulejob(schedulejob_id)"
                        >确认删除</vs-button>
                      </vs-col>

                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="warning"
                          type="filled"
                          @click="popupActiveScheduleJob_del=false"
                        >取消</vs-button>
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
          
      </vs-tab>

      <vs-tab vs-label="触发任务" @click="init_triggerjob_http()"> 
           <div> <br> </div>
          <div class="flex flex-wrap">
            <vs-tabs vs-alignment="fixed">
              <vs-tab vs-label="触发HTTP任务">
                <vs-row>
                  <vs-col vs-type="flex" vs-justify="left" vs-align="center" vs-w="4">
                    <vs-button
                      color="success"
                      type="filled"
                      @click="popupActive_triggerjobcreate()"
                    >新增触发HTTP任务</vs-button>
                  </vs-col>

                  <vs-popup title="创建一个新的触发任务" :active.sync="popupActive_triggerjob">
                    <div class="vx-row">
                      <div class="vx-col w-full">
                        <p>
                          任务名称
                          <font color="#FF0000">*</font>
                        </p>
                        <vs-input v-model="task_title_trigger" class="w-full" />
                        <br />
                      </div>
                      <div class="vx-col w-full">
                        <p>触发数据通道(只能填写上传数据通道ID)</p>
                        <vs-input v-model="trigger_datachannel" class="w-full" />
                        <br />
                      </div>
                      <div class="vx-col w-full">
                        <p>阈值-最大值-最小值</p>
                        <vs-input
                          v-model="trigger_threshold_value"
                          placeholder="阈值"
                          class="w-1/4 vs-col"
                        />
                        <vs-input v-model="trigger_maximum_value" placeholder="最大值" class="w-1/4 vs-col" />
                        <vs-input v-model="trigger_minimum_value" placeholder="最小值" class="w-1/4 vs-col" />
                      </div>
                      <div class="vx-col w-full">
                        <br />
                        <p>
                          选择触发条件
                          <font color="#FF0000">*</font>
                        </p>
                        <v-select
                          autocomplete
                          :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                          v-model="compare_choice"
                        ></v-select>
                        <br />
                      </div>
                    </div>
                    <div class="vx-col w-full">
                      <br />
                      <p>任务运行状态</p>
                      <ul class="centerx">
                        <li>
                          <vs-radio
                            class="vx-col w-1/4 mt-4"
                            color="success"
                            v-model="task_enabled_trigger"
                            vs-value="RUNNING"
                          >运行</vs-radio>
                          <vs-radio
                            class="vx-col w-1/4 mt-4"
                            color="danger"
                            v-model="task_enabled_trigger"
                            vs-value="PAUSING"
                          >暂停</vs-radio>
                        </li>
                      </ul>
                    </div>
                    <div class="vx-col w-full">
                      <br />
                      <p>
                        选择执行动作
                        <font color="#FF0000">*</font>
                      </p>
                      <select
                        autocomplete
                        placeholder="选择执行动作"
                        class="selectExample w-full"
                        v-model="select1_action_trigger"
                        style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                      >
                        <option
                          :key="index"
                          :value="item.id"
                          v-for="(item,index) in options1_action_trigger"
                        >{{ item.title }}</option>
                      </select>
                    </div>

                    <div class="vx-col w-full">
                      <vs-button
                        class="vx-col w-1/3 mt-3"
                        type="border"
                        color="success"
                        v-on:click="addtriggerjob()"
                      >添加触发任务</vs-button>
                    </div>
                  </vs-popup>

                  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
                    <vs-input
                      placeholder="搜索触发任务"
                      v-model="knowledgeBaseSearchQuery_trigger"
                      icon-pack="feather"
                      icon="icon-search"
                      class="w-full no-icon-border mt-4"
                    />
                  </vs-col>
                </vs-row>

                <vs-divider />

                <vs-table pagination max-items="10" :data="filteredKB_trigger" stripe>
                  <template slot="thead">
                    <vs-th>序号</vs-th>
                    <vs-th>任务名称</vs-th>
                    <vs-th>触发设备</vs-th>
                    <vs-th>触发设备通道</vs-th>
                    <vs-th>触发条件</vs-th>
                    <vs-th>触发阈值</vs-th>
                    <vs-th>最大值</vs-th>
                    <vs-th>最小值</vs-th>
                    <vs-th>被触发动作</vs-th>
                    <vs-th>创建时间</vs-th>
                    <vs-th>更新时间</vs-th>
                    <vs-th>状态</vs-th>

                    <vs-th style="padding-left:50px;">操作</vs-th>
                  </template>

                  <template slot-scope="{data}">
                    <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                      <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>

                      <vs-td :data="data[indextr].title">{{ data[indextr].title }}</vs-td>

                      <vs-td :data="data[indextr].device">{{ data[indextr].device }}</vs-td>

                      <vs-td :data="data[indextr].datachannel_title">{{ data[indextr].datachannel_title }}</vs-td>

                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-if="data[indextr].compare_choice=='GREAT_THAN'"
                      >大于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='EQUAL'"
                      >等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='GREAT_EQUAL'"
                      >大于等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='LITTLE_THAN'"
                      >小于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='LITTLE_EQUAL'"
                      >小于等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='BETWEEN_MAX_MIN'"
                      >最大、小值之间</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='NOT_BETWEEN_MAX_MIN'"
                      >最大、小值之外</vs-td>
                      <vs-td :data="data[indextr].threshold_value">{{ data[indextr].threshold_value }}</vs-td>

                      <vs-td :data="data[indextr].maximum">{{ data[indextr].maximum }}</vs-td>

                      <vs-td :data="data[indextr].minimum">{{ data[indextr].minimum }}</vs-td>

                      <vs-td :data="data[indextr].action_title">{{ data[indextr].action_title }}</vs-td>

                      <vs-td :data="data[indextr].created">{{ data[indextr].created | formatDate }}</vs-td>

                      <vs-td :data="data[indextr].updated">{{ data[indextr].updated | formatDate }}</vs-td>

                      <vs-td
                        :data="data[indextr].status_choice"
                        v-if="data[indextr].status_choice=='RUNNING'"
                        class="text-success"
                      >运行</vs-td>
                      <vs-td
                        :data="data[indextr].status_choice"
                        v-else-if="data[indextr].status_choice=='PAUSING'"
                        class="text-warning"
                      >暂停</vs-td>

                      <vs-td>
                        <vs-col
                          v-tooltip="'col - 4'"
                          vs-type="flex"
                          vs-w="2"
                          v-if="tr.status_choice=='PAUSING'"
                        >
                          <span class="text-danger">
                            <vx-tooltip color="success" text="启动任务">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-play"
                                @click="triggerjob_start(tr,indextr)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-else>
                          <span class="text-danger">
                            <vx-tooltip color="warning" text="停止任务">
                              <vs-button
                                radius
                                color="warning"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-pause"
                                @click="triggerjob_stop(tr,indextr)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveTriggerJob_delfunc(tr)"
                              ></vs-button>

                              <vs-popup
                                class="holamundo"
                                title="删除触发任务"
                                :active.sync="popupActiveTriggerJob_del"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delete_triggerjob(triggerjob_id)"
                                    >确认删除</vs-button>
                                  </vs-col>

                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveTriggerJob_del=false"
                                    >取消</vs-button>
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
              </vs-tab>
              <vs-tab vs-label="触发MQTT任务" @click="init_triggermqttlist()">
                <vs-row>
                  <vs-col vs-type="flex" vs-justify="left" vs-align="center" vs-w="4">
                    <vs-button
                      color="success"
                      type="filled"
                      @click="popupActive_triggerjobcreate_mqtt()"
                    >新增触发MQTT任务</vs-button>
                  </vs-col>

                  <vs-popup title="创建一个新的触发任务" :active.sync="popupActive_triggerjob_mqtt">
                    <div class="vx-row">
                      <div class="vx-col w-full">
                        <p>
                          任务名称
                          <font color="#FF0000">*</font>
                        </p>
                        <vs-input v-model="task_title_mqtt" class="w-full" />
                        <br />
                      </div>
                      <div class="vx-col w-full">
                        <p>触发数据通道(只能填写上传数据通道ID)</p>
                        <vs-input v-model="trigger_datachannel_mqtt" class="w-full" />
                        <br />
                      </div>
                      <div class="vx-col w-full">
                        <p>阈值-最大值-最小值</p>
                        <vs-input
                          v-model="trigger_threshold_value_mqtt"
                          placeholder="阈值"
                          class="w-1/4 vs-col"
                        />
                        <vs-input
                          v-model="trigger_maximum_value_mqtt"
                          placeholder="最大值"
                          class="w-1/4 vs-col"
                        />
                        <vs-input
                          v-model="trigger_minimum_value_mqtt"
                          placeholder="最小值"
                          class="w-1/4 vs-col"
                        />
                      </div>
                      <div class="vx-col w-full">
                        <br />
                        <p>
                          选择触发条件
                          <font color="#FF0000">*</font>
                        </p>
                        <v-select
                          autocomplete
                          :options="['GREAT_THAN','EQUAL','GREAT_EQUAL','LITTLE_THAN','LITTLE_EQUAL','BETWEEN_MAX_MIN','NOT_BETWEEN_MAX_MIN']"
                          v-model="compare_choice_mqtt"
                        ></v-select>
                        <br />
                      </div>
                    </div>
                    <div class="vx-col w-full">
                      <br />
                      <p>任务运行状态</p>
                      <ul class="centerx">
                        <li>
                          <vs-radio
                            class="vx-col w-1/4 mt-4"
                            color="success"
                            v-model="task_enabled_mqtt"
                            vs-value="RUNNING"
                          >运行</vs-radio>
                          <vs-radio
                            class="vx-col w-1/4 mt-4"
                            color="danger"
                            v-model="task_enabled_mqtt"
                            vs-value="PAUSING"
                          >暂停</vs-radio>
                        </li>
                      </ul>
                    </div>
                    <div class="vx-col w-full">
                      <br />
                      <p>
                        选择执行动作
                        <font color="#FF0000">*</font>
                      </p>
                      <select
                        autocomplete
                        placeholder="选择执行动作"
                        class="selectExample w-full"
                        v-model="select1_action_mqtt"
                        style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                      >
                        <option
                          :key="index"
                          :value="item.id"
                          v-for="(item,index) in options1_action_mqtt"
                        >{{ item.title }}</option>
                      </select>
                    </div>

                    <div class="vx-col w-full">
                      <vs-button
                        class="vx-col w-1/3 mt-3"
                        type="border"
                        color="success"
                        v-on:click="addtriggerjob_mqtt()"
                      >添加触发任务</vs-button>
                    </div>
                  </vs-popup>

                  <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="8">
                    <vs-input
                      placeholder="搜索触发MQTT任务"
                      v-model="knowledgeBaseSearchQuery_mqtt"
                      icon-pack="feather"
                      icon="icon-search"
                      class="w-full no-icon-border mt-4"
                    />
                  </vs-col>
                </vs-row>

                <vs-divider />

                <vs-table pagination max-items="10" :data="filteredKB_mqtt" stripe>
                  <template slot="thead">
                    <vs-th>序号</vs-th>
                    <vs-th>任务名称</vs-th>
                    <vs-th>触发设备</vs-th>
                    <vs-th>触发设备通道</vs-th>
                    <vs-th>触发条件</vs-th>
                    <vs-th>触发阈值</vs-th>
                    <vs-th>最大值</vs-th>
                    <vs-th>最小值</vs-th>
                    <vs-th>被触发动作</vs-th>
                    <vs-th>创建时间</vs-th>
                    <vs-th>更新时间</vs-th>
                    <vs-th>状态</vs-th>

                    <vs-th style="padding-left:50px;">操作</vs-th>
                  </template>

                  <template slot-scope="{data}">
                    <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                      <vs-td :data="data[indextr].id">{{ data[indextr].id }}</vs-td>

                      <vs-td :data="data[indextr].title">{{ data[indextr].title }}</vs-td>

                      <vs-td :data="data[indextr].device">{{ data[indextr].device }}</vs-td>

                      <vs-td :data="data[indextr].datachannel_title">{{ data[indextr].datachannel_title }}</vs-td>

                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-if="data[indextr].compare_choice=='GREAT_THAN'"
                      >大于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='EQUAL'"
                      >等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='GREAT_EQUAL'"
                      >大于等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='LITTLE_THAN'"
                      >小于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='LITTLE_EQUAL'"
                      >小于等于</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='BETWEEN_MAX_MIN'"
                      >最大、小值之间</vs-td>
                      <vs-td
                        :data="data[indextr].compare_choice"
                        v-else-if="data[indextr].compare_choice=='NOT_BETWEEN_MAX_MIN'"
                      >最大、小值之外</vs-td>

                      <vs-td :data="data[indextr].threshold_value">{{ data[indextr].threshold_value }}</vs-td>

                      <vs-td :data="data[indextr].maximum">{{ data[indextr].maximum }}</vs-td>

                      <vs-td :data="data[indextr].minimum">{{ data[indextr].minimum }}</vs-td>

                      <vs-td :data="data[indextr].action_title">{{ data[indextr].action_title }}</vs-td>

                      <vs-td :data="data[indextr].created">{{ data[indextr].created | formatDate }}</vs-td>

                      <vs-td :data="data[indextr].updated">{{ data[indextr].updated | formatDate }}</vs-td>

                      <vs-td
                        :data="data[indextr].status_choice"
                        v-if="data[indextr].status_choice=='RUNNING'"
                        class="text-success"
                      >运行</vs-td>
                      <vs-td
                        :data="data[indextr].status_choice"
                        v-else-if="data[indextr].status_choice=='PAUSING'"
                        class="text-warning"
                      >暂停</vs-td>

                      <vs-td>
                        <vs-col
                          v-tooltip="'col - 4'"
                          vs-type="flex"
                          vs-w="2"
                          v-if="tr.status_choice=='PAUSING'"
                        >
                          <span class="text-danger">
                            <vx-tooltip color="success" text="启动任务">
                              <vs-button
                                radius
                                color="success"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-play"
                                @click="triggerjob_start_mqtt(tr,indextr)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>
                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2" v-else>
                          <span class="text-danger">
                            <vx-tooltip color="warning" text="停止任务">
                              <vs-button
                                radius
                                color="warning"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-pause"
                                @click="triggerjob_stop_mqtt(tr,indextr)"
                              ></vs-button>
                            </vx-tooltip>
                          </span>
                        </vs-col>

                        <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="2">
                          <span class="text-danger">
                            <vx-tooltip color="danger" text="删除">
                              <vs-button
                                radius
                                color="danger"
                                type="flat"
                                icon-pack="feather"
                                icon="icon-trash"
                                @click="popupActiveTriggerJob_delfunc_mqtt(tr)"
                              ></vs-button>

                              <vs-popup
                                class="holamundo"
                                title="删除触发任务"
                                :active.sync="popupActiveTriggerJob_del_mqtt"
                                background-color="rgba(0,0,0,.1)"
                              >
                                <vs-row vs-justify="center">
                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="danger"
                                      type="filled"
                                      @click="delete_triggerjob_mqtt(triggerjob_id_mqtt)"
                                    >确认删除</vs-button>
                                  </vs-col>

                                  <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                                    <vs-button
                                      color="warning"
                                      type="filled"
                                      @click="popupActiveTriggerJob_del_mqtt=false"
                                    >取消</vs-button>
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
              </vs-tab>
            </vs-tabs>
          
          </div>
      </vs-tab> -->


    </vs-tabs>
  </div>

  
</template>


<script>
/* eslint-disable */
import vSelect from "vue-select";

import ECharts from 'vue-echarts/components/ECharts'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/legend'
import 'echarts/lib/chart/line'
import theme from './theme.json'


import 'echarts/lib/chart/gauge'
import echarts from 'echarts'
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import VuePerfectScrollbar from 'vue-perfect-scrollbar'

import QRCode from 'qrcodejs2'

import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import "flatpickr/dist/flatpickr.min.css";

ECharts.registerTheme('ovilia-green', theme)

var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}

export default {
	data() {


		return {

            selectrow:-1,
            selectrow2:-1,
            dateList2:[],
            valueList2:[],
            url:'',
            deviceName:'',
            deviceId:'',
            deviceDescription:'',
            deviceType:'',
            protocalType:'',
            is_reg:'',
            createdDate:'',
            updatedDate:'',
            dataChannel: [
              {
                "id": 1,
                "title": "Leanne Graham",
                "datatype": "Bret",
                "unitsymbol": "hh",
              },
            ],
            dataChannelTmp:[],

            devTagKey:'',
            devTagValue:'',
            devTagList:[],
            tagkey_input:'',
            tagvalue_input:'',
            tmp_tag:'',
            popupActiveTag_del:false,
            popupActiveTag:false,

            deviceRegCode:'',
            deviceStatus:'',
            onlinedDate:'',
            activatedDate:'',

            //data channel
            select1_datatype:'DECIMAL',
            options1:[
              {text:'数值型',value:'DECIMAL'},
              {text:'开关型',value:'SWITCH'},
              {text:'文本型',value:'MESSAGE'},
              {text:'GPS型',value:'GPS'},
            ],
            datachannelName:'',
            tmp_datach_title:'',
            tmp_datach_id:'',
            index_tmp:'',
            //DataUnits:'',

            //unit
            unitlabel:'',
            unitsymbol:'',
            unitstep:1,
            maxvalue:100,
            minvalue:1,
            //tmp_datachannelid
            tmp_dataid:'',
            popupActive1:false,
            popupActive2:false,
            //control channel
            ctrlChannel: [
              {
                "id": 1,
                "title": "Leanne Graham",
                "datatype": "Bret",
                "unitsymbol": "hh",
              },
            ],
            ctrlChanneltmp:[],
            ctrlchannelName:'',
            select2_datatype:'DECIMAL',
            options2:[
              {text:'数值型',value:'DECIMAL'},
              {text:'开关型',value:'SWITCH'},
              {text:'文本型',value:'MESSAGE'},
              {text:'GPS型',value:'GPS'},
            ],
            popupActive1ctrl:false,
            tmp_ctrlch_title:'',
            tmp_ctrlch_id:'',
            index_tmpctrl:'',

            popupActive2ctrl:false,

            // chart
            popupActiveLine:false,
            tmp_datach_name:'',
            datach_datainput:'',
            echartshow:'',
            echartshow_dchswitch:false,
            center: {lng: 0, lat: 0},
            zoom: 3,
            echartshowmap:false,
            echartshowmsg:'',
            datamsg:[],
            datapoints:[],

            //ctrl
            echartshowctrl:'',
            datamsgctrl:[],
            datamsgctrl_down:[],
            echartshowmsgctrl:'',
            echartshowmapctrl:false,
            datapointsctrl:[],
            //sst2019
            echartshowctrl_down:'',
            echartshowmsgctrl_down:'',
            echartshowmapctrl_down:false,
            datapointsctrl_down:[],

            //interval
            interval_num: 1,
            select_interval: "MINUTES",
            options_interval: [
              { text: "DAYS", value: "DAYS" },
              { text: "HOURS", value: "HOURS" },
              { text: "MINUTES", value: "MINUTES" },
              { text: "SECONDS", value: "SECONDS" },
              { text: "MICROSECONDS", value: "MICROSECONDS" }
            ],
            intervalList: [],
            popupActiveInterval_update: false,
            interval_every:'',
            select1_period:'',
            tmp_interval_id:'',

            configs: {
              dateTimePicker: {
                enableTime: true,
                dateFormat: "Y-m-d H:i"
              }
            },

            form: {
              dateTime: null
            },
            clockedList: [],
            popupActiveClocked_update: false,
            tmp_clocked_id: "",
            popupActiveInterval_del: false,
            popupActiveClocked_del: false,
            crons_minute: "*",
            crons_hour: "*",
            crons_weekday: "*",
            crons_monthday: "*",
            crons_yearmonth: "*",
            cronsList: [],
            popupActiveCrons_del: false,
            tmp_crons_id: "",

            crons_minute_input: "",
            crons_hour_input: "",
            crons_weekday_input: "",
            crons_monthday_input: "",
            crons_yearmonth_input: "",
            popupActiveCrons_update: false,
            //for action
            globalhttpactionList: [],
            showactionparams: false,
            globalact_title: "",
            globalact_url: "",
            popupActiveHttpact_update: false,
            globalhttpaction_id: "",
            globalhttpaction_title: "",
            globalhttpaction_id_tmp: "",
            globalhttpaction_title_tmp: "",
            globalhttpaction_url_tmp: "",
            popupActiveHttpact_del: false,

            httpactparamList: [],
            httpactparamKey: "",
            httpactparamValue: "",
            popupActiveActparam_del: false,
            httpactparam_id: "",
            //以下是MQTT动作数据
            globalmqttactionList: [],
            global_mqtt_act_title: "",
            global_mqtt_topic: "",
            popupActiveMqttact_del: false,
            globalmqttaction_id_tmp: "",

            popupActiveMqttact_update: false,
            globalmqttaction_title_tmp: "",
            globalmqttaction_topic_tmp: "",
            showmqttactionparams: false,
            globalmqttaction_id: "",
            globalmqttaction_title: "",
            mqttactparamList: [],
            mqttactparamKey: "",
            mqttactparamValue: "",
            popupActiveMqttActparam_del: false,

            //for schedule task
            schedulejobsList: [],
        //url: this.GLOBAL.baseURL,
        knowledgeBaseSearchQuery: "",
        popupActive_schedulejob: false,
        schedule_type: "",
        schedule_interval_input: false,
        schedule_cron_input: false,
        schedule_clocked_input: false,
        task_enabled: true,

        configsjob: {
          dateTimePickerJob: {
            enableTime: true,
            dateFormat: "Y-m-d H:i"
          }
        },

        formjob: {
          startdateTimeJob: null,
          enddateTimeJob: null
        },

        select1_action: 0,
        options1_action: [],

        select1_interval: 0,
        options1_interval: [],

        select1_cron: 0,
        options1_cron: [],

        select1_clocked: 0,
        options1_clocked: [],

        task_title: "",
        task_description: "",
        popupActiveScheduleJob_del: false,
        schedulejob_id: "",

        schedule_action_type: "",
        schedule_httpaction_input: false,
        schedule_mqttaction_input: false,
        select2_action: 0,
        options2_action: [],

        //for trigger
        triggerjobsList: [],
        knowledgeBaseSearchQuery_trigger: "",
        popupActive_triggerjob: false,
        task_title_trigger: "",//g
        trigger_datachannel: "",
        trigger_threshold_value: "",
        trigger_maximum_value: "100",
        trigger_minimum_value: "1",
        compare_choice: "GREAT_THAN",

        task_enabled_trigger: true,//g

        select1_action_trigger: 0,//g
        options1_action_trigger: [],//g

        popupActiveTriggerJob_del: false,
        triggerjob_id: "",
        // 以下是mqtt动作任务
        popupActive_triggerjob_mqtt: false,
        select1_action_mqtt: 0,
        options1_action_mqtt: [],
        triggerjobsList_mqtt: [],
        knowledgeBaseSearchQuery_mqtt: "",
        task_title_mqtt: "",
        trigger_datachannel_mqtt: "",
        trigger_threshold_value_mqtt: "",
        trigger_maximum_value_mqtt: "100",
        trigger_minimum_value_mqtt: "1",
        compare_choice_mqtt: "GREAT_THAN",
        task_enabled_mqtt: true,

        popupActiveTriggerJob_del_mqtt: false,
        triggerjob_id_mqtt: "",
        //submit test data
        measurement_test_value:'',
        datachannel_id_tmp:'',
        datachannel_tmp_tr:'',
        //switch status
        switchstatus_test_value:"1",
        //message
        message_test_value:'',
        lng_test_value:'',
        lat_test_value:'',
        addressKeyword:'',
        address_tmp:'',
        //metric data
        metric_test_value:'',
        ctrlchannel_id_tmp:'',
        ctrlchannel_tmp_tr:'',
        metric_test_value_down:'',
        //switch status
        switchdata_test_value:"1",
        echartshow_cchswitch:false,
        echartshow_cchswitch_down:false,
        switchdata_test_value_down:"1",

        message_test_value_ctrl:'',
        message_test_value_ctrl_down:'',

        lng_test_value_ctrl:'',
        lat_test_value_ctrl:'',
        addressKeyword_ctrl:'',
        address_tmp_ctrl:'',

        lng_test_value_ctrl_down:'',
        lat_test_value_ctrl_down:'',
        addressKeyword_ctrl_down:'',
        address_tmp_ctrl_down:'',


            
    }
    

    },

    computed: {
    filteredKB() {
      return this.schedulejobsList.filter(
        item =>
          item.name
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery.toLowerCase()) ||
          item.description
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery.toLowerCase())
      );
    },
    filteredKB_trigger() {
      return this.triggerjobsList.filter(
        item =>
          item.title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase()) ||
          item.datachannel_title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase()) ||
          item.device
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_trigger.toLowerCase())
      );
    },
    filteredKB_mqtt() {
      return this.triggerjobsList_mqtt.filter(
        item =>
          item.title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase()) ||
          item.datachannel_title
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase()) ||
          item.device
            .toLowerCase()
            .includes(this.knowledgeBaseSearchQuery_mqtt.toLowerCase())
      );
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
    mounted: async function() {


      //需要考虑页面跳转时传递设备id参数，当刷新页面时，需要保留设备id号
      var tmp;
      if (!this.$route.params.deviceId) {
         tmp = window.sessionStorage.getItem("deviceId");
      }
      else {
        tmp = this.$route.params.deviceId;    
        window.sessionStorage.setItem("deviceId",this.$route.params.deviceId);
      }
      const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+tmp+'/').catch(function (error) {
			console.log(error)
			return error.response.data;});
			console.log(response)
			if (response.status==200) {
                this.deviceId = response.data.id;
                this.deviceName = response.data.title;
                this.url = this.GLOBAL.baseURL+ response.data.img;
                this.deviceDescription = response.data.description;
                this.deviceType = response.data.device_type;
                this.protocalType = response.data.protocal_type;
                this.is_reg = response.data.is_custom_registered;
                this.createdDate = response.data.created;
                this.updatedDate = response.data.updated;
                this.deviceRegCode = response.data.register_code;
                this.deviceStatus = response.data.status;
                this.onlinedDate = response.data.last_online;
                this.activatedDate = response.data.activated;
      }
      this.getDevTaglist();
      this.getDevDataChannel();
      // this.qrcode();
      return true;

    },
    methods:{

      qrcodeinit(){
         document.getElementById("qrcode").innerHTML = "";
         let qrcode = new QRCode('qrcode', {
        width: 150,
        height: 150, // 高度
        text: this.deviceId,// 二维码内容
        correctLevel: QRCode.CorrectLevel.H
        // render: 'canvas' // 设置渲染方式（有两种方式 table和canvas，默认是canvas）
        // background: '#f0f'
        // foreground: '#ff0'
      })
      console.log(qrcode)

       },


    //   qrcode () {
    //   let qrcode = new QRCode('qrcode', {
    //     width: 150,
    //     height: 150, // 高度
    //     text: this.deviceId// 二维码内容
    //     // render: 'canvas' // 设置渲染方式（有两种方式 table和canvas，默认是canvas）
    //     // background: '#f0f'
    //     // foreground: '#ff0'
    //   })
    //   console.log(qrcode)
    // },

      echartshowlinectrl_no(){

        this.echartshowctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl=false;
        this.echartshow_cchswitch=false;

      },
      echartshowlinectrl_no_down(){

        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshowmapctrl_down=false;

      },


      async echartshowlinectrl(tr,indextr){
          this.selectrow2=indextr;
          this.echartshowctrl=true;
          this.echartshowmapctrl=false;
          this.echartshowmsgctrl=false;
          this.echartshowctrl_down=false;
          this.echartshowmapctrl_down=false;
          this.echartshowmsgctrl_down=false;
          this.echartshow_cchswitch=false;
          this.echartshow_cchswitch_down=false;
          this.ctrlchannel_id_tmp=tr.id;
          this.ctrlchannel_tmp_tr=tr;
          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/metricdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          var tmpdatalist = [];

          for (var tmpdp in response.data){
            if(response.data[tmpdp].direction=='UP'){
              var tmp_timestamp = response.data[tmpdp].timestamp.replace('T',' ').substring(0,19);  
              var tmparr = [tmp_timestamp,response.data[tmpdp].value];
              tmpdatalist.push(tmparr)
            }
          }

         
          var myChart = echarts.init(document.getElementById('echartContainerCtrl'));
          // 绘制图表
          var option={
                  title: { text: "设备上传的数据状态，数据通道名称："+tr.title + "       单位："+tr.unitsymbol,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: tmpdatalist,
                      step:'end',
                      type: 'line'
                  }]
              };
          //option.series[0].step='';
          myChart.setOption(option);

      },

    async echartshowlinectrl_down(tr,indextr){
          this.selectrow2=indextr;
          this.echartshowctrl_down=true;
          this.echartshowmapctrl_down=false;
          this.echartshowmsgctrl_down=false;
          this.echartshowctrl=false;
          this.echartshowmapctrl=false;
          this.echartshowmsgctrl=false;
          this.echartshow_cchswitch=false;
          this.echartshow_cchswitch_down=false;
          this.ctrlchannel_id_tmp=tr.id;
          this.ctrlchannel_tmp_tr=tr;
          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/metricdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          var tmpdatalist = [];

          for (var tmpdp in response.data){
            if(response.data[tmpdp].direction=='DOWN'){
              var tmp_timestamp = response.data[tmpdp].timestamp.replace('T',' ').substring(0,19);  
              var tmparr = [tmp_timestamp,response.data[tmpdp].value];
              tmpdatalist.push(tmparr)
            }
          }

         
          var myChart = echarts.init(document.getElementById('echartContainerCtrl_down'));
          // 绘制图表
          var option={
                  title: { text: "向设备下发的数据指令，数据通道名称："+tr.title + "       单位："+tr.unitsymbol,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: tmpdatalist,
                      step:'end',
                      type: 'line'
                  }]
              };
          //option.series[0].step='';
          myChart.setOption(option);

      },


    async echartshowswitchctrl(tr,indextr){
          this.selectrow2=indextr;
          this.echartshowctrl=false;
          this.echartshowmsgctrl=false;
          this.echartshowmapctrl=false;
          this.echartshowctrl_down=false;
          this.echartshowmsgctrl_down=false;
          this.echartshowmapctrl_down=false;
          this.echartshow_cchswitch_down=false;
          this.echartshow_cchswitch=true;
          this.ctrlchannel_id_tmp=tr.id;
          this.ctrlchannel_tmp_tr=tr;

          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/switchdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          var tmpdatalist = [];

          for (var tmpdp in response.data){
            if(response.data[tmpdp].direction=='UP'){
              var tmp_timestamp = response.data[tmpdp].timestamp.replace('T',' ').substring(0,19);  
              var tmparr = [tmp_timestamp,response.data[tmpdp].switch];
              tmpdatalist.push(tmparr)
            }
          }
          //alert(JSON.stringify(dateList_tmp));
          //alert(valueList_tmp);
          var myChart = echarts.init(document.getElementById('echartContainerCtrl_cchswitch'));
          // 绘制图表
          var option={
                  title: { text: "设备上传的开关状态， 数据通道名称："+tr.title,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: tmpdatalist,
                      step:'start',
                      type: 'line'
                  }]
              };
          myChart.setOption(option);

      },

    //sst20190927
    async echartshowswitchctrl_down(tr,indextr){
          this.selectrow2=indextr;
          this.echartshowctrl_down=false;
          this.echartshowmsgctrl_down=false;
          this.echartshowmapctrl_down=false;
          this.echartshowctrl=false;
          this.echartshowmsgctrl=false;
          this.echartshowmapctrl=false;
          this.echartshow_cchswitch=false;
          this.echartshow_cchswitch_down=true;
          this.ctrlchannel_id_tmp=tr.id;
          this.ctrlchannel_tmp_tr=tr;

          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/switchdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          var tmpdatalist = [];

          for (var tmpdp in response.data){
            if(response.data[tmpdp].direction=='DOWN'){
              var tmp_timestamp = response.data[tmpdp].timestamp.replace('T',' ').substring(0,19);  
              var tmparr = [tmp_timestamp,response.data[tmpdp].switch];
              tmpdatalist.push(tmparr)
            }
          }
          //alert(JSON.stringify(dateList_tmp));
          //alert(valueList_tmp);
          var myChart = echarts.init(document.getElementById('echartContainerCtrl_cchswitch_down'));
          // 绘制图表
          var option={
                  title: { text: "向设备下发的开关数据， 数据通道名称："+tr.title,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: tmpdatalist,
                      step:'start',
                      type: 'line'
                  }]
              };
          myChart.setOption(option);

      },

      async echartshowmsgFunctrl(tr,indextr){
        this.selectrow2=indextr;
        this.echartshowmsgctrl=true;
        this.echartshowmapctrl=false;
        this.echartshowctrl=false;
        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshowmapctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;
        this.ctrlchannel_id_tmp=tr.id;
          this.ctrlchannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/textdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});

        // response.data.forEach(function(item,index,arr) {  
        //       if(item.direction=='DOWN'){
        //       arr.splice(index, 1);  }  
        //      });

        // this.datamsgctrl = response.data;
        var temp_array=[];
        response.data.forEach(function(item) {  
              if(item.direction=='UP'){
              temp_array.push(item);  }  
             });

        this.datamsgctrl = temp_array;


      },

      async echartshowmsgFunctrl_down(tr,indextr){
        this.selectrow2=indextr;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl=false;
        this.echartshowctrl=false;
        this.echartshowmsgctrl_down=true;
        this.echartshowmapctrl_down=false;
        this.echartshowctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;
        this.ctrlchannel_id_tmp=tr.id;
        this.ctrlchannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/textdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});
        var temp_array=[];
        response.data.forEach(function(item) {  
              if(item.direction=='DOWN'){
              temp_array.push(item)
              // arr.splice(index, 1);  
              }  
             });

        //this.datamsgctrl_down = response.data;
        this.datamsgctrl_down = temp_array;


      },

        echartshowmsgctrl_no(){

        this.echartshowctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl=false;
        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshowmapctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;

      },

       echartshowmsgctrl_no_down(){

        this.echartshowctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl=false;
        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshowmapctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;

      },

      async echartshowmapFunctrl(tr,indextr){
        this.selectrow2=indextr;
        this.echartshowmapctrl=false;
        
        this.echartshowctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl_down=false;
        
        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;
        this.ctrlchannel_id_tmp=tr.id;
        this.ctrlchannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/gpsdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});
        var tmparr = [];
        response.data.forEach(function(item) {  
          if(item.direction=='UP'){
              tmparr.push([item.longitude,item.latitude]);
                }
                 
             });
        
        this.datapointsctrl = tmparr;
        this.echartshowmapctrl=true;
      },

      async echartshowmapFunctrl_down(tr,indextr){
        this.selectrow2=indextr;
        this.echartshowmapctrl=false;
        this.echartshowctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowmapctrl_down=false;
        this.echartshowctrl_down=false;
        this.echartshowmsgctrl_down=false;
        this.echartshow_cchswitch=false;
        this.echartshow_cchswitch_down=false;
        this.ctrlchannel_id_tmp=tr.id;
        this.ctrlchannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tr.id +'/gpsdata/').catch(function (error) {
            console.log(error)
            return error.response.data;});
        var tmparr = [];
        response.data.forEach(function(item) {  
          if(item.direction=='DOWN'){
              tmparr.push([item.longitude,item.latitude]);
                }
                 
             });
        this.datapointsctrl_down = tmparr;
        this.echartshowmapctrl_down=true;
      },

      handlerctrl ({BMap,map}) {
        console.log(BMap, map)

        this.center.lng = 116.404
        this.center.lat = 39.915
        this.zoom = 6

        // map.centerAndZoom(new BMap.Point(106.486654,29.490295), 6);
        // map.enableScrollWheelZoom();
        // alert("ddd")
        // var pointA = new BMap.Point(106.486654,29.490295);  // 创建点坐标A--大渡口区
        // var pointB = new BMap.Point(106.581515,29.615467);  // 创建点坐标B--江北区
        //   //alert('从大渡口区到江北区的距离是：'+(map.getDistance(pointA,pointB)).toFixed(2)+' 米。');  //获取两点距离,保留小数点后两位
        // var polyline = new BMap.Polyline([pointA,pointB], {strokeColor:"blue", strokeWeight:6, strokeOpacity:0.5});  //定义折线
        // map.addOverlay(polyline);     //添加折线到地图上

        // map.centerAndZoom(new BMap.Point(106.486654,29.490295), 6);
        // map.enableScrollWheelZoom();

        if(this.datapointsctrl){
          var tmp = this.datapointsctrl;
          var top_left_navigation = new BMap.NavigationControl(); 
          map.addControl(top_left_navigation);  

          var points = [];
          for ( var i = 0; i <tmp.length; i++){
                points.push(new BMap.Point(tmp[i][0],tmp[i][1]))
            }

          this.center.lng = points[0].lng
          this.center.lat = points[0].lat
          var marker = new BMap.Marker(points[0]);
          map.addOverlay(marker); 
          var marker2 = new BMap.Marker(points[tmp.length-1]);
          map.addOverlay(marker2); 
          marker.setAnimation(BMAP_ANIMATION_BOUNCE); 
      
          var polyline2 = new BMap.Polyline(points, {strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});  //定义折线
          map.addOverlay(polyline2);     //添加折线到地图上

        }
        },

        handlerctrl_down ({BMap,map}) {
        console.log(BMap, map)

        this.center.lng = 116.404
        this.center.lat = 39.915
        this.zoom = 6

        // map.centerAndZoom(new BMap.Point(106.486654,29.490295), 6);
        // map.enableScrollWheelZoom();
        // alert("ddd")
        // var pointA = new BMap.Point(106.486654,29.490295);  // 创建点坐标A--大渡口区
        // var pointB = new BMap.Point(106.581515,29.615467);  // 创建点坐标B--江北区
        //   //alert('从大渡口区到江北区的距离是：'+(map.getDistance(pointA,pointB)).toFixed(2)+' 米。');  //获取两点距离,保留小数点后两位
        // var polyline = new BMap.Polyline([pointA,pointB], {strokeColor:"blue", strokeWeight:6, strokeOpacity:0.5});  //定义折线
        // map.addOverlay(polyline);     //添加折线到地图上

        // map.centerAndZoom(new BMap.Point(106.486654,29.490295), 6);
        // map.enableScrollWheelZoom();

        if(this.datapointsctrl_down){
          var tmp = this.datapointsctrl_down;
          var top_left_navigation = new BMap.NavigationControl(); 
          map.addControl(top_left_navigation);  

          var points = [];
          for ( var i = 0; i <tmp.length; i++){
                points.push(new BMap.Point(tmp[i][0],tmp[i][1]))
            }

          this.center.lng = points[0].lng
          this.center.lat = points[0].lat
          var marker = new BMap.Marker(points[0]);
          map.addOverlay(marker); 
          var marker2 = new BMap.Marker(points[tmp.length-1]);
          map.addOverlay(marker2); 
          marker.setAnimation(BMAP_ANIMATION_BOUNCE); 
      
          var polyline2 = new BMap.Polyline(points, {strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});  //定义折线
          map.addOverlay(polyline2);     //添加折线到地图上

        }
        },

      echartshowmapctrl_no(){

        this.echartshowctrl=false;
        this.echartshowmapctrl=false;
        this.echartshowmsgctrl=false;
        this.echartshowctrl_down=false;
        this.echartshowmapctrl_down=false;
        this.echartshowmsgctrl_down=false;

      },


      async echartshowmsgFun(tr,indextr){
        this.selectrow = indextr;
        this.echartshowmsg=true;
        this.echartshowmap=false;
        this.echartshow=false;
        this.echartshowmsg_down=false;
        this.echartshowmap_down=false;
        this.echartshow_down=false;
        this.echartshow_dchswitch=false;
        this.datachannel_id_tmp=tr.id;
        this.datachannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/'+tr.id +'/messages/').catch(function (error) {
            console.log(error)
            return error.response.data;});

        this.datamsg = response.data;


      },

      async echartshowmapFun(tr,indextr){
        this.selectrow = indextr;
        this.echartshowmap=false;
        this.echartshow=false;
        this.echartshowmsg=false;
        this.echartshowmap_down=false;
        this.echartshow_down=false;
        this.echartshowmsg_down=false;
        this.echartshow_dchswitch=false;
        this.datachannel_id_tmp=tr.id;
        this.datachannel_tmp_tr=tr;
        const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/'+tr.id +'/position/').catch(function (error) {
            console.log(error)
            return error.response.data;});

        response.data.forEach(function(item,index,arr) {  
              var tmparr = [];
              tmparr = [item.longitude,item.latitude];
              arr.splice(index, 1,tmparr);    
             });
        this.datapoints = response.data;
        this.echartshowmap=true;


      },


      handler ({BMap,map}) {
        console.log(BMap, map)

				this.center.lng = 116.404
				this.center.lat = 39.915
        this.zoom = 6

        if(this.datapoints){
          var tmp = this.datapoints;
          var top_left_navigation = new BMap.NavigationControl(); 
          map.addControl(top_left_navigation);  

          var points = [];
          for ( var i = 0; i <tmp.length; i++){
                points.push(new BMap.Point(tmp[i][0],tmp[i][1]))
            }
            
          this.center.lng = points[0].lng
          this.center.lat = points[0].lat
          var marker = new BMap.Marker(points[0]);
          map.addOverlay(marker); 
          var marker2 = new BMap.Marker(points[tmp.length-1]);
          map.addOverlay(marker2); 
          marker2.setAnimation(BMAP_ANIMATION_BOUNCE); 
      
          var polyline2 = new BMap.Polyline(points, {strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});  //定义折线
          map.addOverlay(polyline2);     //添加折线到地图上

        }
        

        },
        
      async echartshowline(tr,indextr){
          this.selectrow = indextr;
          this.echartshow=true;
          this.echartshowmap=false;
          this.echartshowmsg=false;
          this.echartshow_dchswitch=false;
          this.datachannel_id_tmp=tr.id;
          this.datachannel_tmp_tr=tr;
          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/'+tr.id +'/measurements/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          response.data.forEach(function(item,index,arr) {  
              var tmparr = [];
              var tmp_timestamp = item.timestamp.replace('T',' ').substring(0,19);
              tmparr = [tmp_timestamp,item.value];
              arr.splice(index, 1,tmparr);   
             });
          this.measurement_point_list = response.data;
          //alert(JSON.stringify(dateList_tmp));
          //alert(valueList_tmp);
          var myChart = echarts.init(document.getElementById('echartContainer'));
          // 绘制图表
          var option={
                  title: { text: "数据通道名称："+tr.title + "       单位："+tr.unitsymbol,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: response.data,
                      type: 'line'
                  }]
              };
          option.series[0].step='';
          myChart.setOption(option);

      },

      async echartshowswitch(tr,indextr){
        this.selectrow = indextr;
          this.echartshow=false;
          this.echartshowmap=false;
          this.echartshowmsg=false;
          this.echartshow_dchswitch=true;
          this.datachannel_id_tmp=tr.id;
          this.datachannel_tmp_tr=tr;

          const response = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/'+tr.id +'/switchstatus/').catch(function (error) {
            console.log(error)
            return error.response.data;});

          response.data.forEach(function(item,index,arr) {  
              var tmparr = [];
              var tmp_timestamp = item.timestamp.replace('T',' ').substring(0,19);
              //alert(tmp_timestamp)
              tmparr = [tmp_timestamp,item.status];
              
              arr.splice(index, 1,tmparr);   
             });
          //alert(JSON.stringify(dateList_tmp));
          //alert(valueList_tmp);
          var myChart = echarts.init(document.getElementById('echartContainer_dchswitch'));
          // 绘制图表
          var option={
                  title: { text: "数据通道名称："+tr.title,left:'center' },
                  tooltip: {},
                  dataZoom: [
                      {   // 这个dataZoom组件，默认控制x轴。
                          type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                          start: 0,      // 左边在 10% 的位置。
                          end: 100         // 右边在 60% 的位置。
                      }
                  ],
                  xAxis: {
                      type: 'category',
                      splitLine: {
                          show: false
                      }
                  },
                  yAxis: {
                      type: 'value'
                  },
                  series: [{
                      data: response.data,
                      step:'start',
                      type: 'line'
                  }]
              };
          myChart.setOption(option);

      },

      echartshowline_no(){

        this.echartshow=false;
        this.echartshowmap=false;
        this.echartshow_dchswitch=false;

      },

      echartshowmap_no(){

        this.echartshow=false;
        this.echartshowmap=false;
        this.echartshow_dchswitch=false;

      },
       echartshowmsg_no(){

        this.echartshow=false;
        this.echartshowmap=false;
        this.echartshowmsg=false;
        this.echartshow_dchswitch=false;

      },


      async adddevtags(param) {
         //alert(param);
         var params ={"device":param,"key":this.devTagKey,"value":this.devTagValue}
         const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+param+'/devicetags/',params).catch(function (error) {
				console.log(error)
        return error.response.data;});
        if(response.status == 201){
          //insert first 
          this.devTagList.splice(0,0,response.data);
          //alert(JSON.stringify(response.data));
          this.devTagKey='';
          this.devTagValue='';
        }
        
        //alert(JSON.stringify(response.data));

       },

      popupActiveTag1(param1){
         this.popupActiveTag=true;
         this.tmp_tag = param1.id;
         this.tagkey_input = param1.key;
         this.tagvalue_input = param1.value;


       },

      popupActiveTag2(param1){
         this.popupActiveTag_del=true;
         this.tmp_tag = param1.id;
         this.tagkey_input = param1.key;
         this.tagvalue_input = param1.value;

       },

      async getDevTaglist(){

        const response_devtags = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/devicetags/').catch(function (error) {
			console.log(error)
      return error.response_devtags.data;});
      if (response_devtags.status == 200 && response_devtags.data != ''){
        this.devTagList = response_devtags.data;
        //alert(JSON.stringify(response_tpltags.data));
       
      }

      },

      async getDevDataChannel(){

      const response_datachannel = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/').catch(function (error) {
			console.log(error)
			return error.response_datachannel.data;});
      console.log(response_datachannel)
      if (response_datachannel.status == 200) {
                this.dataChannel =  response_datachannel.data;
                
      }

      for(var tmp_index in this.dataChannel) {
        var tmp_channel_id = this.dataChannel[tmp_index].id;
       
      const response_unit = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/datachannels/'+tmp_channel_id+'/dataunits/').catch(function (error) {
			console.log(error)
      return error.response_unit.data;});
      if (response_unit.status == 200 && response_unit.data != ''){        
        this.dataChannel[tmp_index].unitsymbol = response_unit.data[0].symbol;
       
      }
      }
      this.dataChannelTmp = this.dataChannel;

    
      },

      async deldevtag(param){
         var tagid = param;
         var devid = this.deviceId;
         var url = this.GLOBAL.baseURL+'/devices/'+devid+'/devicetags/'+tagid+'/';
                  this.popupActiveTag_del=false;
          await this.axios.delete(url).then(function(response) {
            console.log(response);
          });
          //删除数组中的元素
          this.devTagList.forEach(function(item, index, arr) {
                if(item.id == tagid) {
                    arr.splice(index, 1);
                }
            });

          return true;

       },

      async devtag_update(param){
         //alert(param.tmp_tag_param);
         //alert(param.tmp_tag_index_param);
         var tagid = param;
         var devid = this.deviceId;
         var tagkey = this.tagkey_input;
         var tagvalue = this.tagvalue_input;
         var params = {"device":devid,"key":tagkey,"value":tagvalue};

         const response = await this.axios.patch(this.GLOBAL.baseURL+'/devices/'+devid+'/devicetags/'+tagid+'/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});

              //删除数组中的元素
          this.devTagList.forEach(function(item, index, arr) {
                if(item.id == tagid) {
                    arr.splice(index, 1,response.data);
                }
            });
          this.popupActiveTag=false;
          return true;
       },

    async adddatachannel() {
          var tmp;
          if (!this.$route.params.deviceId) {
            tmp = window.sessionStorage.getItem("deviceId")
          }
          else {
            tmp = this.$route.params.deviceId;
            window.sessionStorage.setItem("deviceId",this.$route.params.deviceId);
          } 
          //alert(tmp)
          if (this.datachannelName) {

              var params = {"device":tmp,"title":this.datachannelName,"datatype":this.select1_datatype};

              const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+tmp+'/datachannels/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});
              if (response.status==201) {
                this.dataChannelTmp.unshift(response.data);
                this.datachannelName = '';
              } 
          }
          else {
            alert("通道名称不能为空！");
          }
       },

    async deldatachannel(param) {

          var devid= this.deviceId;
          var datachn = param;

          var url = this.GLOBAL.baseURL+'/devices/'+devid+'/datachannels/'+datachn+'/';
          await this.axios.delete(url).then(function(response) {
            console.log(response);
            alert("已删除")
          });
           
          //删除数组中的元素
          this.dataChannelTmp.forEach(function(item, index, arr) {
                if(item.id == datachn) {
                    arr.splice(index, 1);
                }
            });
       },

    popupActiveF(param,param2) {

         this.popupActive1=true;
         this.tmp_datach_id = param.id;
         this.tmp_datach_title = param.title;
         this.index_tmp=param2;

       },
    
    async tmp_datach_update(param) {
         var devid = this.deviceId;
         var datachid=param;
         var params = {"title":this.tmp_datach_title};

         const response = await this.axios.patch(this.GLOBAL.baseURL+'/devices/'+devid+'/datachannels/'+datachid+'/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});

         this.popupActive1 = false;

         this.dataChannelTmp.forEach(function(item, index, arr) {
                if(item.id == datachid) {
                    //arr.splice(index, 1,response.data);
                    arr[index].title = response.data.title;
                }
            });
       },

    //ADD UNIT
    popupActiveF2(param) {
         this.popupActive2=true;
         this.tmp_dataid = param.id; 
       },
    

    async adddataunit(param) {
         
         var devid = this.deviceId;
         var tpl_dataid =param;

         
        this.popupActive2=false;
         
        var params ={"datachannel":tpl_dataid,"unitlabel":this.unitlabel,"symbol":this.unitsymbol,"max_value":this.maxvalue,"min_value":this.minvalue,"step":this.unitstep}
        //alert(JSON.stringify(params))
        const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+devid+'/datachannels/'+tpl_dataid+'/dataunits/',params).catch(function (error) {
				console.log(error)
        return error.response.data;});

        //alert(response.status);

        //删除数组中的元素
        if(response.status=='201'){
           this.dataChannelTmp.forEach(function(item, index, arr) {
                if(item.id == tpl_dataid) {
                  arr[index].unitsymbol = response.data.symbol;
                }
            });
        }

         // this.tmpdataChannel=this.dataChannel;
        //window.location.reload();

       },

       async ctrlchannelinit(){
         this.echartshow=false;
        this.echartshowmap=false;
        this.echartshowmsg=false;
        this.echartshowctrl=false;
        this.echartshowmapctrl=false;
        this.echartshowmsgctrl=false;

         const response_ctrlchannel = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/').catch(function (error) {
        console.log(error)
        return error.response_ctrlchannel.data;});
        console.log(response_ctrlchannel)
        if (response_ctrlchannel.status == 200) {
                  this.ctrlChannel =  response_ctrlchannel.data;
                  
        }
        for(var tmp_index in this.ctrlChannel) {
          var tmp_channel_id = this.ctrlChannel[tmp_index].id;
        
        const response_unit = await this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.deviceId+'/ctrlchannels/'+tmp_channel_id+'/ctrlunits/').catch(function (error) {
        console.log(error)
        return error.response_unit.data;});
        if (response_unit.status == 200 && response_unit.data != ''){        
          this.ctrlChannel[tmp_index].unitsymbol = response_unit.data[0].symbol;
        
        }
        }
        this.ctrlChanneltmp = this.ctrlChannel;
       },

      //以下是控制通道

       async addctrlchannel() {
          var tmp;
          if (!this.$route.params.templateId) {
            tmp = window.sessionStorage.getItem("deviceId")
          }
          else {
            tmp = this.$route.params.templateId;
            window.sessionStorage.setItem("deviceId",this.$route.params.deviceId);
          } 

          if (this.ctrlchannelName) {

              var params = {"device":tmp,"title":this.ctrlchannelName,"datatype":this.select2_datatype};

              const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+tmp+'/ctrlchannels/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});
              if (response.status==201) {
                this.ctrlChanneltmp.unshift(response.data);
                this.ctrlchannelName = '';
              } 
          }
          else {
            alert("通道名称不能为空！");
          }
       },
    //ADD UNIT
    popupActiveF2ctrl(param) {
         this.popupActive2ctrl=true;
         this.tmp_ctrlchid = param.id; 
       },

  async delctrlchannel(param) {

          var devid= this.deviceId;
          var ctrlchn = param;
          var url = this.GLOBAL.baseURL+'/devices/'+devid+'/ctrlchannels/'+ctrlchn+'/';
          await this.axios.delete(url).then(function(response) {
            console.log(response);
            alert("已删除")
          });
           
          //删除数组中的元素
          this.ctrlChanneltmp.forEach(function(item, index, arr) {
                if(item.id == ctrlchn) {
                    arr.splice(index, 1);
                }
            });
       },

    popupActiveFctrl(param,param2) {

         this.popupActive1ctrl=true;
         this.tmp_ctrlch_id = param.id;
         this.tmp_ctrlch_title = param.title;
         this.index_tmpctrl=param2;

       },
    async tmp_ctrlch_update(param) {
         var devid = this.deviceId;
         var ctrlchid=param;
         var params = {"title":this.tmp_ctrlch_title};

         const response = await this.axios.patch(this.GLOBAL.baseURL+'/devices/'+devid+'/ctrlchannels/'+ctrlchid+'/',params).catch(function (error) {
              console.log(error)
              return error.response.data;});

         this.popupActive1ctrl = false;

         this.ctrlChanneltmp.forEach(function(item, index, arr) {
                if(item.id == ctrlchid) {
                    //arr.splice(index, 1,response.data);
                    arr[index].title = response.data.title;
                }
            });
       },

       async addctrlunit(param) {
         
         var devid = this.deviceId;
         var tpl_ctrlchid =param;

         
        this.popupActive2ctrl=false;
         
        var params ={"ctrlchannel":tpl_ctrlchid,"unitlabel":this.unitlabel,"symbol":this.unitsymbol,"max_value":this.maxvalue,"min_value":this.minvalue,"step":this.unitstep}
        //alert(JSON.stringify(params))
        const response = await this.axios.post(this.GLOBAL.baseURL+'/devices/'+devid+'/ctrlchannels/'+tpl_ctrlchid+'/ctrlunits/',params).catch(function (error) {
				console.log(error)
        return error.response.data;});

        //alert(response.status);

        //删除数组中的元素
        if(response.status=='201'){
           this.ctrlChanneltmp.forEach(function(item, index, arr) {
                if(item.id == tpl_ctrlchid) {
                  arr[index].unitsymbol = response.data.symbol;
                }
            });
        }
       },
             // 时间计划
      async init_schedule(){
        const response = await this.axios
      .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/intervalscheduledev/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    console.log(response);
    this.intervalList = response.data;
      },

      async addinterval() {
      var params = {
        every: this.interval_num,
        period: this.select_interval.toLowerCase(),
        device:this.deviceId,
        owner: 1
      };
      const response = await this.axios
        .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/intervalscheduledev/", params)
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.intervalList.unshift(response.data);
    },

    popupActiveInterval_delfunc(tag) {
      this.tmp_interval_id = tag.id;
      this.popupActiveInterval_del = true;
    },
    async delinterval(tmp_interval_id) {
      var url =
        this.GLOBAL.baseURL + "/trigger/intervals_top/"+ tmp_interval_id + "/";
      this.popupActiveInterval_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.intervalList.forEach(function(item, index, arr) {
        if (item.id == tmp_interval_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

     popupActiveInterval_updatefunc(tag) {
      this.popupActiveInterval_update = true;
      this.select1_period = tag.period.toUpperCase();
      this.interval_every = tag.every;
      this.tmp_interval_id = tag.id;
    },
    async interval_update(tmp_interval_id) {
      // let params = new FormData();

      // params.append('every', this.interval_every) // 添加form表单中其他数据
      // params.append('period',this.select1_period.toLowerCase())

      var params = {
        every: this.interval_every,
        period: this.select1_period.toLowerCase()
      };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/intervalscheduledev/" + tmp_interval_id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.intervalList.forEach(function(item, index, arr) {
        if (item.id == tmp_interval_id) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveInterval_update = false;
      return true;
    },
    //clocked
    async clockedinit() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/clockedscheduledev/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.clockedList = response.data;
    },

    async addclocked() {
      if (this.form.dateTime != null) {
        var params = { clocked_time: new Date(this.form.dateTime), device:this.deviceId,owner: 1 };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/clockedscheduledev/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.clockedList.unshift(response.data);
      }
      return true;
    },

    popupActiveClocked_delfunc(tag) {
      this.tmp_clocked_id = tag.id;
      this.popupActiveClocked_del = true;
    },
    async delclocked(tmp_clocked_id) {
      var url =
        this.GLOBAL.baseURL + "/trigger/clocked_top/" + tmp_clocked_id + "/";
      this.popupActiveClocked_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.clockedList.forEach(function(item, index, arr) {
        if (item.id == tmp_clocked_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    popupActiveClocked_updatefunc(tag) {
      this.popupActiveClocked_update = true;
      //alert(this.formatDateM(tag.clocked_time))
      this.form.dateTime = this.formatDateM(tag.clocked_time);
      this.tmp_clocked_id = tag.id;
    },
    async Clocked_update(tmp_clocked_id) {
      var params = { clocked_time: new Date(this.form.dateTime) };
      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/clockedscheduledev/" + tmp_clocked_id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.clockedList.forEach(function(item, index, arr) {
        if (item.id == tmp_clocked_id) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveClocked_update = false;
      return true;
    },

    formatDateM: function(val) {
      var value = new Date(val);
      var year = value.getFullYear();
      var month = padDate(value.getMonth() + 1);
      var day = padDate(value.getDate());
      var hour = padDate(value.getHours());
      var minutes = padDate(value.getMinutes());
      //var seconds=padDate(value.getSeconds());
      return year + "-" + month + "-" + day + " " + hour + ":" + minutes;
    },

    async cronsinit() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/crontabscheduledev/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.cronsList = response.data;
    },

    async addcrons() {
      var params = {
        minute: this.crons_minute,
        hour: this.crons_hour,
        day_of_week: this.crons_weekday,
        day_of_month: this.crons_monthday,
        month_of_year: this.crons_yearmonth,
        device: this.deviceId,
        owner: 1
      };
      const response = await this.axios
        .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/crontabscheduledev/", params)
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.cronsList.unshift(response.data);
      this.crons_minute = "*";
      this.crons_hour = "*";
      this.crons_weekday = "*";
      this.crons_monthday = "*";
      this.crons_yearmonth = "*";
    },

     popupActiveCrons_delfunc(tag) {
      this.tmp_crons_id = tag.id;
      this.popupActiveCrons_del = true;
    },
    async delcrons(tmp_crons_id) {
      var url = this.GLOBAL.baseURL + "/trigger/crons_top/" + tmp_crons_id + "/";
      this.popupActiveCrons_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.cronsList.forEach(function(item, index, arr) {
        if (item.id == tmp_crons_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    popupActiveCrons_updatefunc(tag) {
      this.popupActiveCrons_update = true;
      this.crons_minute_input = tag.minute;
      this.crons_hour_input = tag.hour;
      this.crons_weekday_input = tag.day_of_week;
      this.crons_monthday_input = tag.day_of_month;
      this.crons_yearmonth_input = tag.month_of_year;
      this.tmp_crons_id = tag.id;
    },

    async Crons_update(tmp_crons_id) {
      var params = {
        minute: this.crons_minute_input,
        hour: this.crons_hour_input,
        day_of_week: this.crons_weekday_input,
        day_of_month: this.crons_monthday_input,
        month_of_year: this.crons_yearmonth_input
      };
      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/crontabscheduledev/" + tmp_crons_id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.cronsList.forEach(function(item, index, arr) {
        if (item.id == tmp_crons_id) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveCrons_update = false;
      return true;
    },

    //for actions
    async init_httpaction(){
      const response = await this.axios
      .get(this.GLOBAL.baseURL +  "/devices/"+this.deviceId+"/devicehttpactions/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    console.log(response);
    this.globalhttpactionList = response.data;
    },
    async show_actionparams(tag) {
      this.showactionparams = true;
      this.globalhttpaction_id = tag.id;
      this.globalhttpaction_title = tag.title;

      const response = await this.axios
        .get(
          this.GLOBAL.baseURL +
            "/trigger/globalhttpaction/" +
            tag.id +
            "/httpkeyvalue/"
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.httpactparamList = response.data;
    },

    async addglobalhttpaction() {
      if (this.globalact_title !='' && this.globalact_url !='') {
        var params = {
          title: this.globalact_title,
          url: this.globalact_url,
          device:this.deviceId,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicehttpactions/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.globalhttpactionList.unshift(response.data);
      }
      else {
        this.$vs.notify({
            title:'提醒：',
            text:'HTTP动作名称、动作URL都不能为空.',
            color:'danger'
          })
      }

      this.globalact_title = "";
      this.globalact_url = "";
    },

    popupActiveHttpact_updatefunc(tag) {
      this.popupActiveHttpact_update = true;
      this.globalhttpaction_id_tmp = tag.id;
      this.globalhttpaction_title_tmp = tag.title;
      this.globalhttpaction_url_tmp = tag.url;
    },

    async globalhttpaction_update(globalhttpaction_id_tmp) {
      let params = new FormData();

      params.append("title", this.globalhttpaction_title_tmp); // 添加form表单中其他数据
      params.append("url", this.globalhttpaction_url_tmp);

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL +
            "/devices/"+this.deviceId+"/devicehttpactions/" +
            globalhttpaction_id_tmp +
            "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.globalhttpactionList.forEach(function(item, index, arr) {
        if (item.id == globalhttpaction_id_tmp) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveHttpact_update = false;
      return true;
    },

    popupActiveHttpact_delfunc(tag) {
      this.popupActiveHttpact_del = true;
      this.globalhttpaction_id_tmp = tag.id;
    },

    async delglobalhttpact(globalhttpaction_id_tmp) {
      var url =
        this.GLOBAL.baseURL +
        "/devices/"+this.deviceId+"/devicehttpactions/" +
        globalhttpaction_id_tmp +
        "/";
      this.popupActiveHttpact_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.globalhttpactionList.forEach(function(item, index, arr) {
        if (item.id == globalhttpaction_id_tmp) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async addhttpactparam(globalhttpaction_id) {
      if (this.httpactparamKey && this.httpactparamValue) {
        var params = {
          key: this.httpactparamKey,
          value: this.httpactparamValue,
          action: globalhttpaction_id
        };
        const response = await this.axios
          .post(
            this.GLOBAL.baseURL +
              "/trigger/globalhttpaction/" +
              globalhttpaction_id +
              "/httpkeyvalue/",
            params
          )
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.httpactparamList.unshift(response.data);
      }

      this.httpactparamKey = "";
      this.httpactparamValue = "";
    },

    popupActiveActparam_func(tr) {
      this.popupActiveActparam_del = true;
      this.httpactparam_id = tr.id;
    },

    async delactparam(httpactparam_id) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalhttpaction/" +
        this.globalhttpaction_id +
        "/httpkeyvalue/" +
        httpactparam_id +
        "/";
      this.popupActiveActparam_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.httpactparamList.forEach(function(item, index, arr) {
        if (item.id == httpactparam_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    //以下是MQTT方法
    async init_mqtt_action() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicemqttactions/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.globalmqttactionList = response.data.reverse();
    },

    async addglobalmqttaction() {
      if (this.global_mqtt_act_title !='' && this.global_mqtt_topic !='') {
        var params = {
          title: this.global_mqtt_act_title,
          topic: this.global_mqtt_topic,
          device:this.deviceId,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicemqttactions/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.globalmqttactionList.unshift(response.data);
      }
      else {
        this.$vs.notify({
            title:'提醒：',
            text:'MQTT动作名称、主题Topic都不能为空.',
            color:'danger'
          })
      }

      this.global_mqtt_act_title = "";
      this.global_mqtt_topic = "";
    },

    popupActiveMqttpact_delfunc(tag) {
      this.popupActiveMqttact_del = true;
      this.globalmqttaction_id_tmp = tag.id;
    },

    async delglobalmqttact(globalmqttaction_id_tmp) {
      var url =
        this.GLOBAL.baseURL +
        "/devices/"+this.deviceId+"/devicemqttactions/" +
        globalmqttaction_id_tmp +
        "/";
      this.popupActiveMqttact_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.globalmqttactionList.forEach(function(item, index, arr) {
        if (item.id == globalmqttaction_id_tmp) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    popupActiveMqttact_updatefunc(tag) {
      this.popupActiveMqttact_update = true;
      this.globalmqttaction_id_tmp = tag.id;
      this.globalmqttaction_title_tmp = tag.title;
      this.globalmqttaction_topic_tmp = tag.topic;
    },

    async globalmqttaction_update(globalmqttaction_id_tmp) {
      let params = new FormData();

      params.append("title", this.globalmqttaction_title_tmp); // 添加form表单中其他数据
      params.append("topic", this.globalmqttaction_topic_tmp);

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL +
            "/devices/"+this.deviceId+"/devicemqttactions/" +
            globalmqttaction_id_tmp +
            "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });

      this.globalmqttactionList.forEach(function(item, index, arr) {
        if (item.id == globalmqttaction_id_tmp) {
          arr.splice(index, 1, response.data);
        }
      });

      this.popupActiveMqttact_update = false;
      return true;
    },

    async show_mqttactionparams(tag) {
      this.showmqttactionparams = true;
      this.globalmqttaction_id = tag.id;
      this.globalmqttaction_title = tag.title;

      const response = await this.axios
        .get(
          this.GLOBAL.baseURL +
            "/trigger/globalmqttaction/" +
            tag.id +
            "/mqttkeyvalue/"
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.mqttactparamList = response.data;
    },

    async addmqttactparam(globalmqttaction_id) {
      if (this.mqttactparamKey && this.mqttactparamValue) {
        var params = {
          key: this.mqttactparamKey,
          value: this.mqttactparamValue,
          action: globalmqttaction_id
        };
        const response = await this.axios
          .post(
            this.GLOBAL.baseURL +
              "/trigger/globalmqttaction/" +
              globalmqttaction_id +
              "/mqttkeyvalue/",
            params
          )
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.mqttactparamList.unshift(response.data);
      }

      this.mqttactparamKey = "";
      this.mqttactparamValue = "";
    },

    popupActiveMqttActparam_func(tr) {
      this.popupActiveMqttActparam_del = true;
      this.mqttactparam_id = tr.id;
    },
    async delmqttactparam(mqttactparam_id) {
      var url =
        this.GLOBAL.baseURL +
        "/trigger/globalmqttaction/" +
        this.globalmqttaction_id +
        "/mqttkeyvalue/" +
        mqttactparam_id +
        "/";
      this.popupActiveMqttActparam_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.mqttactparamList.forEach(function(item, index, arr) {
        if (item.id == mqttactparam_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    //for schedule task
     async showschedule_actioninput() {
      if (this.schedule_action_type == "HTTP") {
        this.schedule_httpaction_input = true;
        this.schedule_mqttaction_input = false;
      }
      if (this.schedule_action_type == "MQTT") {
        this.schedule_httpaction_input = false;
        this.schedule_mqttaction_input = true;
      }
    },

    async showscheduleinput() {
      if (this.schedule_type == "INTERVAL") {
        this.schedule_interval_input = true;
        this.schedule_cron_input = false;
        this.schedule_clocked_input = false;
      }
      if (this.schedule_type == "CRONS") {
        this.schedule_interval_input = false;
        this.schedule_cron_input = true;
        this.schedule_clocked_input = false;
      }
      if (this.schedule_type == "CLOCKED") {
        this.schedule_interval_input = false;
        this.schedule_cron_input = false;
        this.schedule_clocked_input = true;
      }
    },

    async popupActive_schedulejobcreate() {
      this.popupActive_schedulejob = true;
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/intervalscheduledev/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.options1_interval = response.data;

      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicehttpactions/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action = response2.data;

      const response3 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/clockedscheduledev/")
        .catch(function(error) {
          console.log(error);
          return error.response3.data;
        });
      console.log(response3);
      this.options1_clocked = response3.data;

      const response4 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/crontabscheduledev/")
        .catch(function(error) {
          console.log(error);
          return error.response4.data;
        });
      console.log(response4);
      this.options1_cron = response4.data;

      const response5 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicemqttactions/")
        .catch(function(error) {
          console.log(error);
          return error.response5.data;
        });
      console.log(response5);
      this.options2_action = response5.data;
    },

    async addschedulejob() {
      if (
        this.task_title &&
        (this.select1_action || this.select2_action) &&
        (this.select1_interval || this.select1_clocked || this.select1_cron)
      ) {
        var tmp;
        var tmp_task;
        if (this.schedule_action_type == "HTTP") {
          tmp = { http_action: this.select1_action };
          tmp_task = "trigger.tasks.globalhttptask";
        }
        if (this.schedule_action_type == "MQTT") {
          tmp = { mqtt_action: this.select2_action };
          tmp_task = "trigger.tasks.globalmqtttask";
        }

        var interval_tmp;
        var cron_tmp;
        var clocked_tmp;
        if (this.select1_interval == "") {
          interval_tmp = "";
        } else {
          interval_tmp = this.select1_interval;
        }
        if (this.select1_cron == "") {
          cron_tmp = "";
        } else {
          cron_tmp = this.select1_cron;
        }
        if (this.select1_clocked == "") {
          clocked_tmp = "";
        } else {
          clocked_tmp = this.select1_clocked;
        }

        var params = {
          name: this.task_title,
          task: tmp_task,
          interval: interval_tmp,
          crontab: cron_tmp,
          clocked: clocked_tmp,
          description: this.task_description,
          enabled: this.task_enabled,
          expires: new Date(this.formjob.enddateTimeJob),
          start_time: new Date(this.formjob.startdateTimeJob),
          kwargs: JSON.stringify(tmp),
          device:this.deviceId,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/periodictaskdev/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
          console.log(response.data)

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/periodictaskdev/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.schedulejobsList = response2.data.reverse();

        this.popupActive_schedulejob = false;
        return true;
      }
      else {
        this.$vs.notify({
            title:'提醒：',
            text:'计划任务名称、时间计划、动作都不能为空.',
            color:'danger'
          })
      }
    },

    popupActiveScheduleJob_delfunc(tr) {
      this.popupActiveScheduleJob_del = true;
      this.schedulejob_id = tr.id;
    },

    async delete_schedulejob(schedulejob_id) {
      var url =
        this.GLOBAL.baseURL + "/trigger/periodtask_top/" + schedulejob_id + "/";
      this.popupActiveScheduleJob_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.schedulejobsList.forEach(function(item, index, arr) {
        if (item.id == schedulejob_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async schedulejob_start(tr, indextr) {
      var params = { enabled: true };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/periodictaskdev/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.schedulejobsList[indextr].enabled = true;
      }
    },

    async schedulejob_stop(tr, indextr) {
      var params = { enabled: false };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/periodictaskdev/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.schedulejobsList[indextr].enabled = false;
      }
    },

    async initschedulejob(){
      const response = await this.axios
      .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/periodictaskdev/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    this.schedulejobsList = response.data;
    },

    // for trigger
    async popupActive_triggerjobcreate() {
      this.popupActive_triggerjob = true;
      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicehttpactions/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action_trigger = response2.data;
    },

    async addtriggerjob() {
      if (
        this.task_title_trigger &&
        this.select1_action_trigger &&
        this.trigger_datachannel &&
        this.trigger_threshold_value
      ) {
        var params = {
          title: this.task_title_trigger,
          datachannel: this.trigger_datachannel,
          threshold_value: this.trigger_threshold_value,
          maximum: this.trigger_maximum_value,
          minimum: this.trigger_minimum_value,
          action: this.select1_action_trigger,
          status_choice: this.task_enabled_trigger,
          compare_choice: this.compare_choice,
          device:this.deviceId,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList = response2.data;

        this.popupActive_triggerjob = false;
        return true;
      }
      else{
        this.$vs.notify({
            title:'提醒：',
            text:'触发任务名称、触发通道、阈值都不能为空.',
            color:'danger'
          })
      }
    },

    popupActiveTriggerJob_delfunc(tr) {
      this.popupActiveTriggerJob_del = true;
      this.triggerjob_id = tr.id;
    },

    async delete_triggerjob(triggerjob_id) {
      var url =
        this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/" + triggerjob_id + "/";
      this.popupActiveTriggerJob_del = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.triggerjobsList.forEach(function(item, index, arr) {
        if (item.id == triggerjob_id) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async triggerjob_start(tr, indextr) {
      var params = { status_choice: "RUNNING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList[indextr].status_choice = "RUNNING";
      }
    },

    async triggerjob_stop(tr, indextr) {
      var params = { status_choice: "PAUSING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList[indextr].status_choice = "PAUSING";
      }
    },

    //以下是MQTT动作任务
    async popupActive_triggerjobcreate_mqtt() {
      this.popupActive_triggerjob_mqtt = true;
      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicemqttactions/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action_mqtt = response2.data;
    },
    async init_triggermqttlist() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobmqtt/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.triggerjobsList_mqtt = response.data;
    },

    async addtriggerjob_mqtt() {
      if (
        this.task_title_mqtt &&
        this.select1_action_mqtt &&
        this.trigger_datachannel_mqtt &&
        this.trigger_threshold_value_mqtt
      ) {
        var params = {
          title: this.task_title_mqtt,
          datachannel: this.trigger_datachannel_mqtt,
          threshold_value: this.trigger_threshold_value_mqtt,
          maximum: this.trigger_maximum_value_mqtt,
          minimum: this.trigger_minimum_value_mqtt,
          action: this.select1_action_mqtt,
          status_choice: this.task_enabled_mqtt,
          compare_choice: this.compare_choice_mqtt,
          device:this.deviceId,
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobmqtt/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobmqtt/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.triggerjobsList_mqtt = response2.data;

        this.popupActive_triggerjob_mqtt = false;
        return true;
      }
      else{
        this.$vs.notify({
            title:'提醒：',
            text:'触发任务名称、触发通道、阈值都不能为空.',
            color:'danger'
          })
      }
    },
    popupActiveTriggerJob_delfunc_mqtt(tr) {
      this.popupActiveTriggerJob_del_mqtt = true;
      this.triggerjob_id_mqtt = tr.id;
    },
    async delete_triggerjob_mqtt(triggerjob_id_mqtt) {
      var url =
        this.GLOBAL.baseURL +
        "/devices/"+this.deviceId+"/devicetriggerjobmqtt/" +
        triggerjob_id_mqtt +
        "/";
      this.popupActiveTriggerJob_del_mqtt = false;
      await this.axios.delete(url).then(function(response) {
        console.log(response);
      });
      //删除数组中的元素

      //删除数组中的元素
      this.triggerjobsList_mqtt.forEach(function(item, index, arr) {
        if (item.id == triggerjob_id_mqtt) {
          arr.splice(index, 1);
        }
      });

      return true;
    },

    async triggerjob_start_mqtt(tr, indextr) {
      var params = { status_choice: "RUNNING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobmqtt/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList_mqtt[indextr].status_choice = "RUNNING";
      }
    },

    async triggerjob_stop_mqtt(tr, indextr) {
      var params = { status_choice: "PAUSING" };

      const response = await this.axios
        .patch(
          this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobmqtt/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.triggerjobsList_mqtt[indextr].status_choice = "PAUSING";
      }
    },
    async init_triggerjob_http(){
      const response = await this.axios
      .get(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/devicetriggerjobhttp/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    this.triggerjobsList = response.data;
    },

    async input_measurement_testvalue(){
      var params = {
          datachannel: this.datachannel_id_tmp,
          value: this.measurement_test_value
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/datachannels/"+this.datachannel_id_tmp+"/measurements/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowline(this.datachannel_tmp_tr);

    },

    async input_switchstatus_testvalue(){
      var params = {
          datachannel: this.datachannel_id_tmp,
          status:  Number(this.switchstatus_test_value),
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/datachannels/"+this.datachannel_id_tmp+"/switchstatus/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowswitch(this.datachannel_tmp_tr);

    },

    async input_message_testvalue(){
      var params = {
          datachannel: this.datachannel_id_tmp,
          message:  this.message_test_value,
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/datachannels/"+this.datachannel_id_tmp+"/messages/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmsgFun(this.datachannel_tmp_tr);

    },

    getLocationPoint(e) {
      this.lng_test_value = e.point.lng;
      this.lat_test_value = e.point.lat;
    },

    getLocationPoint_ctrl(e) {
      this.lng_test_value_ctrl = e.point.lng;
      this.lat_test_value_ctrl = e.point.lat;
    },

     getLocationPoint_ctrl_down(e) {
      this.lng_test_value_ctrl_down = e.point.lng;
      this.lat_test_value_ctrl_down = e.point.lat;
    },

    async input_position_testvalue(){
      var params = {
          datachannel: this.datachannel_id_tmp,
          latitude:this.lat_test_value,
          longitude:this.lng_test_value,
          address:this.address_tmp,
          elevation:'1'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/datachannels/"+this.datachannel_id_tmp+"/position/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmapFun(this.datachannel_tmp_tr);

    },

    async input_metric_testvalue(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          value: this.metric_test_value,
          direction:'UP'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/metricdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowlinectrl(this.ctrlchannel_tmp_tr);

    },

    async input_metric_testvalue_down(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          value: this.metric_test_value_down,
          direction:'DOWN'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/metricdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowlinectrl_down(this.ctrlchannel_tmp_tr);

    },

    async input_switchdata_testvalue(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          switch:  Number(this.switchdata_test_value),
          direction:'UP'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/switchdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowswitchctrl(this.ctrlchannel_tmp_tr);

    },

    async input_switchdata_testvalue_down(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          switch:  Number(this.switchdata_test_value_down),
          direction:'DOWN'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/switchdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowswitchctrl_down(this.ctrlchannel_tmp_tr);

    },

    async input_message_testvalue_ctrl(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          text:  this.message_test_value_ctrl,
          direction:'UP'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/textdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmsgFunctrl(this.ctrlchannel_tmp_tr);

    },

    async input_message_testvalue_ctrl_down(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          text:  this.message_test_value_ctrl_down,
          direction:'DOWN'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/textdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmsgFunctrl_down(this.ctrlchannel_tmp_tr);

    },

    async input_position_testvalue_ctrl(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          latitude:this.lat_test_value_ctrl,
          longitude:this.lng_test_value_ctrl,
          address:this.address_tmp_ctrl,
          elevation:'1',
          direction:'UP'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/gpsdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmapFunctrl(this.ctrlchannel_tmp_tr);

    },

    async input_position_testvalue_ctrl_down(){
      var params = {
          ctrlchannel: this.ctrlchannel_id_tmp,
          latitude:this.lat_test_value_ctrl_down,
          longitude:this.lng_test_value_ctrl_down,
          address:this.address_tmp_ctrl_down,
          elevation:'1',
          direction:'DOWN'
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/devices/"+this.deviceId+"/ctrlchannels/"+this.ctrlchannel_id_tmp+"/gpsdata/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        console.log(response.data);
        this.echartshowmapFunctrl_down(this.ctrlchannel_tmp_tr);

    },

   async  test_actionstatus(tag) {

      const response = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/globalhttpactions/"+tag.id+"/status")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
      alert(response.data.status)

   }


   },

   components: {
      "v-select": vSelect,
    ECharts,
    BaiduMap,
    VuePerfectScrollbar ,
    flatPickr
  }
}
</script>