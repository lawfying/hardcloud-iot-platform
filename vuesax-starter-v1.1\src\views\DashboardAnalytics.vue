<!-- =========================================================================================
	File Name: DashboardAnalytics.vue
	Description: Dashboard Analytics
	----------------------------------------------------------------------------------------
	Item Name: Vuesax Admin - VueJS Dashboard Admin Template
	Version: 1.1
	Author: Pixinvent
	Author URL: hhttp://www.themeforest.net/user/pixinvent
========================================================================================== -->
<template>
	<div id="dashboard-analytics">
		<div class="vx-row">
            <div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="UsersIcon" :statistic="db_num.num" statisticTitle="设备绑定者数量" :chartData="subscribersGained" type='area'></statistics-card-line>
			</div>
			<div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="MapIcon" :statistic="db_num.sce_num" statisticTitle="应用绑定者数量" :chartData="subscribersGainedSce" color='warning' type='area'></statistics-card-line>
			</div>
            <div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="ShoppingBagIcon" :statistic="db_num.dev_num" :statisticTitle="'已创建设备,激活'+db_num.dev_num_active+'个设备。'" :chartData="subscribersGainedDev" color='warning' type='area'></statistics-card-line>
			</div>
            <div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="CodesandboxIcon" :statistic="db_num.sceapp_num" statisticTitle="已创建应用场景" :chartData="subscribersGainedSceapp" type='area'></statistics-card-line>
			</div>

			<div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="ApertureIcon" :statistic="db_num.dch_num" statisticTitle="已创建数据通道" :chartData="subscribersGainedDch" color='warning' type='area'></statistics-card-line>
			</div>

            <div class="vx-col w-full sm:w-1/6 md:w-1/6 lg:w-1/6 xl:w-1/6 mb-base">
				<statistics-card-line icon="TargetIcon" :statistic="db_num.cch_num" statisticTitle="已创建控制通道" :chartData="subscribersGainedCch" type='area'></statistics-card-line>
			</div>
        </div>
        <div class="vx-row">
            <div class="row-box">
                <div class="vx-col chartsBox mb-base" v-for="(item,index) in chartsList" :key="index">
                    <img src="../assets/images/raty/add.png" alt=""  @click="addEcharts(index)" v-if="item.showIcon">
                    <div :id="item.id" style="width:480px; height:250px" v-if="item.showCharts"></div>
                    <baidu-map  ak='2140eb7ba44386b17ef7f6601239b6b9' :center="center" :zoom="zoom"  @ready="handlerctrl"  style="width:100%;height:300px;" v-if="item.mapShow"  :scroll-wheel-zoom="true">
                    </baidu-map>
                    <div v-if="item.showList" style="width:100%;height:100%; overflow-y: auto;" class="textList">
                        <div class="textBox " :key="indexmsg" v-for="(msg, indexmsg) in datamsgctrl">
                                <div class="textIcon">
                                   <img src="../assets/images/logo/warn.png" alt="">
                                </div>
                            <div class="textContent">
                                <div class="textarea">
                                    {{ msg.text }}
                                </div>
                                <div>
                                    {{msg.timestamp | formatDate }}
                                </div>
                            </div>
                        </div>
                    </div>
                    <img src="../assets/images/pages/close.png" alt="" v-show="!item.showIcon" @click="deleteCharts(index)" class="closeIcon">
                </div>
            </div>
        </div>
        
        <vs-popup   title="新增" :active.sync="addChartsShow">
            <div class="popContent" v-if="showCharts" style="width:10rem">
                 <vs-select autocomplete label="设备名称" placeholder="选择设备名称"  v-model="equipName">
                    <vs-select-item
                        :key="index"
                        :value="item.value"
                        :text="item.text"
                        v-for="(item,index) in options1"
                    />
                    </vs-select>
                    <vs-select autocomplete label="通道名称" placeholder="选择通道名称"  v-model="wayName">
                        <vs-select-item
                            :key="index"
                            :value="item.value"
                            :text="item.text"
                            v-for="(item,index) in options2"
                        />
                    </vs-select>
                     <vs-select   autocomplete label="设备发送类型" placeholder="选择设备发送类型"  v-model="chartsType">
                        <vs-select-item
                            :key="index"
                            :value="item.value"
                            :text="item.text"
                            v-for="(item,index) in options3"
                        />
                    </vs-select>
                     <vs-button style="margin-top:20px;" color="success" size="small" type="filled" @click="createDevices()">添加图表</vs-button>
            </div>
        </vs-popup>
               
	</div>
</template>

<script>
/* eslint-disable */ 
import VueApexCharts from 'vue-apexcharts'
import echarts from 'echarts'
import StatisticsCardLine from '@/components/statistics-cards/StatisticsCardLine.vue'
import ChangeTimeDurationDropdown from '@/components/ChangeTimeDurationDropdown.vue'
import Vue from 'vue'
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
var padDate = function(va){
  va=va<10?'0'+va:va;
  return va
}
export default{
	data() {
		return {
            chartsList:[
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts1',
                    mapShow:false,
                    showList:false,
                },
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts2',
                    mapShow:false,
                    showList:false,
                },
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts3',
                    mapShow:false,
                    showList:false,
                },
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts4',
                    mapShow:false,
                    showList:false,
                },
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts5',
                    mapShow:false,
                    showList:false,
                },
                {
                    showIcon:true,
                    showCharts:false,
                    id:'charts6',
                    mapShow:false,
                    showList:false,
                },
            ],
            options1:[],
            options2:[
                {text:'暂无数据',value:0}
            ],
            showIcon:true,
            baiduMapShow:false,
            options3:[
                {text:'上传数据',value:'UP'},
                {text:'下发数据',value:'DOWN'}
            ],
            datamsgctrl:[],
            equipName:'',
            boxIndex:null,
            wayName:'',
            chartsType:'',
            center: {lng: 0, lat: 0},
            zoom: 3,
            showCharts:true,
            addChartsShow:false,
			db_num:'',
			card_7: {
				overlay_img: 'card-image-6.jpg',
				title: '硬云物联网平台',
				text: "YINGCLOUD IOT，硬云物联网平台，快速接入您的设备与应用。采用MongoDB数据库，支持海量传感数据；采用PostgreSQL,支持关系型数据处理；支持HTTP、MQTT协议，快速接入设备与应用。采用 JSON Web Token身份认证，用户通过具有时间有效期限制的token进行访问REST API资源。",
			},
			subscribersGained: {
            series: [{
                name: '设备绑定用户',
                data: [10,2,10,2,10,2,10]
            }],
            chartOptions: {
                grid: {
                    show: false,
                    padding: {
                        left: 0,
                        right: 0
                    }
                },
                chart: {
                    toolbar: {
                        show: false,
                    },
                    sparkline: {
                        enabled: true
                    }
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth',
                    width: 2.5
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shadeIntensity: 0.9,
                        opacityFrom: 0.7,
                        opacityTo: 0.5,
                        stops: [0, 80, 100]
                    }
                },
                xaxis: {
                    type: 'numeric',
                    lines: {
                        show: false,
                    },
                    axisBorder: {
                        show: false,
                    },
                    labels: { show: false }
                },
                yaxis: [{
                    y: 0,
                    offsetX: 0,
                    offsetY: 0,
                    padding: { left: 0, right: 0 },
                }],
                tooltip: {
                    x: { show: false }
                },
            },
	    },
	

        subscribersGainedSce: {
            series: [{
                name: '应用绑定用户',
                data: [10,2,10,2,10,2,10]
            }],
            chartOptions: {
                grid: {
                    show: false,
                    padding: {
                        left: 0,
                        right: 0
                    }
                },
                chart: {
                    toolbar: {
                        show: false,
                    },
                    sparkline: {
                        enabled: true
                    }
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth',
                    width: 2.5
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        shadeIntensity: 0.9,
                        opacityFrom: 0.7,
                        opacityTo: 0.5,
                        stops: [0, 80, 100]
                    }
                },
                xaxis: {
                    type: 'numeric',
                    lines: {
                        show: false,
                    },
                    axisBorder: {
                        show: false,
                    },
                    labels: { show: false }
                },
                yaxis: [{
                    y: 0,
                    offsetX: 0,
                    offsetY: 0,
                    padding: { left: 0, right: 0 },
                }],
                tooltip: {
                    x: { show: false }
                },
            },
        },
	
		subscribersGainedDev: {
        series: [{
            name: '设备数量',
            data: [10,2,10,2,10,2,10]
        }],
        chartOptions: {
            grid: {
                show: false,
                padding: {
                    left: 0,
                    right: 0
                }
            },
            chart: {
                toolbar: {
                    show: false,
                },
                sparkline: {
                    enabled: true
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 2.5
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 0.9,
                    opacityFrom: 0.7,
                    opacityTo: 0.5,
                    stops: [0, 80, 100]
                }
            },
            xaxis: {
                type: 'numeric',
                lines: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                labels: { show: false }
            },
            yaxis: [{
                y: 0,
                offsetX: 0,
                offsetY: 0,
                padding: { left: 0, right: 0 },
            }],
            tooltip: {
                x: { show: false }
            },
        },
        },

            subscribersGainedSceapp: {
                series: [{
                    name: '应用场景',
                    data: [10,2,10,2,10,2,10]
                }],
                chartOptions: {
                    grid: {
                        show: false,
                        padding: {
                            left: 0,
                            right: 0
                        }
                    },
                    chart: {
                        toolbar: {
                            show: false,
                        },
                        sparkline: {
                            enabled: true
                        }
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        curve: 'smooth',
                        width: 2.5
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 0.9,
                            opacityFrom: 0.7,
                            opacityTo: 0.5,
                            stops: [0, 80, 100]
                        }
                    },
                    xaxis: {
                        type: 'numeric',
                        lines: {
                            show: false,
                        },
                        axisBorder: {
                            show: false,
                        },
                        labels: { show: false }
                    },
                    yaxis: [{
                        y: 0,
                        offsetX: 0,
                        offsetY: 0,
                        padding: { left: 0, right: 0 },
                    }],
                    tooltip: {
                        x: { show: false }
                    },
                },
            },
            
            subscribersGainedDch: {
                series: [{
                    name: '数据通道',
                    data: [10,2,10,2,10,2,10]
                }],
                chartOptions: {
                    grid: {
                        show: false,
                        padding: {
                            left: 0,
                            right: 0
                        }
                    },
                    chart: {
                        toolbar: {
                            show: false,
                        },
                        sparkline: {
                            enabled: true
                        }
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        curve: 'smooth',
                        width: 2.5
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 0.9,
                            opacityFrom: 0.7,
                            opacityTo: 0.5,
                            stops: [0, 80, 100]
                        }
                    },
                    xaxis: {
                        type: 'numeric',
                        lines: {
                            show: false,
                        },
                        axisBorder: {
                            show: false,
                        },
                        labels: { show: false }
                    },
                    yaxis: [{
                        y: 0,
                        offsetX: 0,
                        offsetY: 0,
                        padding: { left: 0, right: 0 },
                    }],
                    tooltip: {
                        x: { show: false }
                    },
                },
            },
            
        subscribersGainedCch: {
                series: [{
                    name: '控制通道',
                    data: [10,2,10,2,10,2,10]
                }],
                chartOptions: {
                    grid: {
                        show: false,
                        padding: {
                            left: 0,
                            right: 0
                        }
                    },
                    chart: {
                        toolbar: {
                            show: false,
                        },
                        sparkline: {
                            enabled: true
                        }
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        curve: 'smooth',
                        width: 2.5
                    },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            shadeIntensity: 0.9,
                            opacityFrom: 0.7,
                            opacityTo: 0.5,
                            stops: [0, 80, 100]
                        }
                    },
                    xaxis: {
                        type: 'numeric',
                        lines: {
                            show: false,
                        },
                        axisBorder: {
                            show: false,
                        },
                        labels: { show: false }
                    },
                    yaxis: [{
                        y: 0,
                        offsetX: 0,
                        offsetY: 0,
                        padding: { left: 0, right: 0 },
                    }],
                    tooltip: {
                        x: { show: false }
                    },
                },
            },
        }
    },
    watch:{
        equipName:{
            handler(val,oldval){
                if(val!=''){
                    this.$nextTick(()=>{
                    this.options2=[]
                    })
                    this.changeEquip();
                }
            }
        },
        // wayName:{
        //     handler(val,oldval){
        //         if(val!=''){
        //             this.options3=[
        //                 {text:'上传数据',value:'UP'},
        //                 {text:'下发数据',value:'DOWN'}
        //             ]
        //         }
        //     }
        // }
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
    created(){
        this.getBasicInfo();
    },
	mounted: async function() {
			const response = await this.axios.get(this.GLOBAL.baseURL+"/dashboard/dashboard_num").catch(function (error) {
				console.log(error)
				return error.response.data;});
			if (response.status==200) {
                this.db_num = response.data;
                //this.subscribersGained.series[0].data=response.data.last5mon;
                Vue.set(this.subscribersGained.series,0,{name: '近5月设备绑定用户',data: response.data.last5mon});
                //this.subscribersGainedSce.series[0].data=response.data.sce_last5mon;
                Vue.set(this.subscribersGainedSce.series,0,{name: '近5月应用绑定用户',data: response.data.sce_last5mon});
                //this.subscribersGainedDev.series[0].data=response.data.dev_last5mon;
                Vue.set(this.subscribersGainedDev.series,0,{name: '近5月设备数量',data: response.data.dev_last5mon});
                //this.subscribersGainedSceapp.series[0].data=response.data.sceapp_last5mon;
                Vue.set(this.subscribersGainedSceapp.series,0,{name: '近5月应用场景',data: response.data.sceapp_last5mon});
                //this.subscribersGainedDch.series[0].data=[0,0,0,0,response.data.dch_num];
                Vue.set(this.subscribersGainedDch.series,0,{name: '数据通道',data: [0,0,0,0,response.data.dch_num]});
                //this.subscribersGainedCch.series[0].data=[0,0,0,0,response.data.cch_num];
                Vue.set(this.subscribersGainedCch.series,0,{name: '控制通道',data: [0,0,0,0,response.data.cch_num]});
            } 
	},
	components: {
		VueApexCharts,
		StatisticsCardLine,
		ChangeTimeDurationDropdown,
        BaiduMap
    },
    methods:{
        // 获取初始化数据
        getBasicInfo(){
            this.axios.get(this.GLOBAL.baseURL+'/devices/').then(res=>{
                if(res.status==200&&res.data){
                    res.data.forEach((item,index)=>{
                        this.options1.push({text:item.title,value:item.id})
                    })
                }
            })
        },
        // 打开选择图表弹窗
        addEcharts(index){
            this.addChartsShow=true;
            this.boxIndex=index;
        },
        // 设备选择
        changeEquip(){
            this.options2=[]
            if(this.equipName){
                this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.equipName+'/ctrlchannels/').then(res=>{
                    if(res.status==200&&res.data.length>0){
                        console.log('options2res',res.data)
                        res.data.forEach((item,index)=>{
                            // if(item.datatype=='DECIMAL'||item.datatype=='SWITCH'){
                             this.options2.push({text:item.title,value:item.id,type:item.datatype})
                        // }
                        })
                        console.log(this.options2,'options2');
                    }
                }).catch(err=>{
                    console.log('rr',err)
                    return
                })
            }
                
        },
        // 初始化图表
        initCharts(id,chartsData,dataName,dataUnit){
            console.log('unit',dataUnit)
             var tmpdatalist = [];
            for (var tmpdp in chartsData){
              var tmp_timestamp = chartsData[tmpdp].timestamp.replace('T',' ').substring(0,19);  
              var tmparr = [tmp_timestamp,chartsData[tmpdp].value];
              tmpdatalist.push(tmparr)
          }
             var myChart = echarts.init(document.getElementById(id));
          // 绘制图表
          var option={
                  title: { 
                    text: `设备上传的数据状态，数据通道名称：${dataName}        单位：${dataUnit?dataUnit:''}`,
                    left:'center', 
                    textStyle:{
                        fontSize:14
                    }
                  },
                  tooltip: {
                        trigger: 'axis'
                    },
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
                      },
                       axisLine: {
                      lineStyle: {
                          color: 'darkgrey'
                      }
                    },
                      axisTick: {
                          show: false
                      },
                      axisLabel: {
                          interval: 0,
                          textStyle: {
                              color: 'black'
                          },
                          margin: 15
                      },
                          boundaryGap: false
                  },
                  yAxis: {
                      type: 'value',
                       splitLine: {
                          show: false
                      },
                       axisLine: {
                      lineStyle: {
                          color: 'darkgrey'
                      }
                    },
                  },
                  series: [{
                      data: tmpdatalist,
                      // step:'end',
                      type: 'line',
                        symbolSize: 6,
                      symbol: 'circle',
                      smooth: false,//是否平滑曲线显示。
                      lineStyle: {
                          color: '#28c76f'
                      },
                      itemStyle: {
                          normal: {
                              color: '#28c76f',
                              borderColor: '#28c76f'
                          }
                        },
                      areaStyle: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#28c76f'
                                    },
                                    {
                                        offset: 1,
                                        color: 'white'
                                    }
                                ])
                        },
              emphasis: {
                  itemStyle: {
                      color: {
                              type: 'radial',
                              x: 0.5,
                              y: 0.5,
                              r: 0.5,
                              colorStops: [{
                                      offset: 0,
                                      color: '#28c76f'
                                  },
                                  {
                                      offset: 0.4,
                                      color: '#60cc90'
                                  },
                                  {
                                      offset: 0.5,
                                      color: '#7ccca0'
                                  }, {
                                      offset: 0.7,
                                      color: '#fff'
                                  }, {
                                      offset: 0.8,
                                      color: '#fff'
                                  }, {
                                      offset: 1,
                                      color: '#fff'
                                  }
                              ]
                          },
                    borderColor: '#28c76f',
                    borderWidth: 2
            }
        }
                  }]
              };
          //option.series[0].step='';
          myChart.setOption(option);
        },
        // 初始化地图
        handlerctrl ({BMap,map}) {
        console.log(BMap, map)
        this.center.lng = 116.404
        this.center.lat = 39.915
        this.zoom = 4
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
        openNotification(position = null, color, icon,text) {
          const noti = this.$vs.notification({
            icon,
            color,
            position,
            text,
          })
        },
        // 新建模板图表
        createDevices(){
            for(let i=0;i<this.options2.length;i++){
                if(this.options2[i].value==this.wayName){
                    console.log('type',this.options2[i].type);
                    // 地图型
                    if(this.options2[i].type=='GPS'){
                        this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.equipName+'/ctrlchannels/'+this.wayName +'/gpsdata/').then(res=>{
                            console.log('gpsdata',res);
                            console.log('dec',this.chartsType);
                             var tmparr = [];
                            res.data.forEach(item=>{  
                                if(item.direction==this.chartsType){
                                    tmparr.push([item.longitude,item.latitude]);
                                }      
                            });
                            this.datapointsctrl= tmparr;
                            this.chartsList[this.boxIndex].showIcon=false
                            this.chartsList[this.boxIndex].mapShow=true
                            this.addChartsShow=false
                        })
                        // 文本型
                    }else if(this.options2[i].type=='MESSAGE'){
                        this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.equipName+'/ctrlchannels/'+this.wayName+'/textdata/').then(res=>{
                            console.log(res,'res');
                            var temp_array=[];
                            res.data.forEach(item=>{  
                            if(item.direction==this.chartsType){
                                temp_array.push(item);  }  
                            });
                            this.datamsgctrl = temp_array;
                            this.chartsList[this.boxIndex].showIcon=false
                            this.chartsList[this.boxIndex].showList=true
                            this.addChartsShow=false
                        })
                        
                    }else if(this.options2[i].type=='SWITCH'||this.options2[i].type=='DECIMAL'){
                        // 图表型
                        this.chartsList[this.boxIndex].showCharts=true
                        this.chartsList[this.boxIndex].showIcon=false
                        console.log('switch/decimal');
                        this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.equipName+'/ctrlchannels/'+this.wayName+'/metricdata/').then(res=>{
                            if(res.status==200&&res.data){
                                this.axios.get(this.GLOBAL.baseURL+'/devices/'+this.equipName+'/ctrlchannels/'+this.wayName+'/ctrlunits/').then(ress=>{
                                    console.log(ress,'ress');
                                let list=[]
                                res.data.forEach(item=>{
                                    if(item.direction==this.chartsType){
                                        list.push(item)
                                    }
                                })
                                console.log('liust',list)
                                
                                var name="";
                                this.options2.forEach(item=>{
                                    if(item.value==this.wayName){
                                        name=item.text
                                    }
                                })
                                var unit;
                                if(ress.data[0]&&ress.data[0].symbol){
                                    unit=ress.data[0].symbol
                                }else{
                                    unit=''
                                }
                                this.initCharts(this.chartsList[this.boxIndex].id,list,name,unit)
                                })
                                this.addChartsShow=false
                            }
                        })
                    }
                    
                     break;
                     
                }
                
            }
            

        },
        // 删除模板图表
        deleteCharts(index){
            this.chartsList[index].showIcon=true
            this.chartsList.splice(index,1)
            var num;
            num=this.chartsList[this.chartsList.length-1].id.substr(6,1)
            console.log(num)
            this.chartsList.push({
                    showIcon:true,
                    showCharts:false,
                    id:`charts${num+1}`,
                     mapShow:false,
                },)
        },
    }
}
</script>

<style lang="scss" scoped>
/deep/ .BMap_mask{
    width: 480px;
    height: 280px;
}
     /deep/ .vs-select--options{
        z-index:53100 !important;
    }
    .con-vs-popup .vs-popup{
        width: 300px;
    }
.vx-row{
    .row-box{
        width: 100%;
        padding: 0 1rem;
        display: flex;
        justify-content: space-between;
        flex-flow: wrap;
    }

    .chartsBox{
        width: 500px;
        height: 300px;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        background:white;
        position:relative;
        // border: 1px solid darkgray;
        box-sizing: border-box;
        position: relative;
        .closeIcon{
            position: absolute;
            width: 20px;
            height: 20px;
            right: 20px;
            top: 20px;
        }
        img{
            width: 80px;
            height: 80px;
        }
    }
}

#dashboard-analytics {
	.greet-user{
		position: relative;
		.decore-left{
			position: absolute;
			left:0;
			top: 0;
		}
		.decore-right{
			position: absolute;
			right:0;
			top: 0;
		}
	}

	@media(max-width: 576px) {
		.decore-left, .decore-right{
			width: 140px;
		}
	}
}
.textList{
    position: absolute;
    left: 0;
    overflow-x: hidden;
    .textBox{
        width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 5px 10px 0;
        margin-bottom: 5px 0;
        .textIcon{
            width: 40px;
            height: 40px;
            background-color:#28c76f;
            border-radius: 50%;
            line-height: 47px;
            img{
                width: 40%;
                height: 40%;
            }
        }
        .textContent{
            padding:0 20px;
            text-align: left;
            flex: 1;
            .textarea{
                width:380px;
                overflow: hidden;
                text-overflow:ellipsis; 
                white-space: nowrap;
            }
        }
    }
}

</style>