<template>
  <div class="mt-5">
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
              :config="configs.dateTimePickerJob"
              id="datetime-input"
              class="form-control"
              v-model="form.startdateTimeJob"
              placeholder="选择时间"
              style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
            ></flat-pickr>
            <br />
          </div>
          <div class="vx-col w-full">
            <br />
            <p>任务结束时间</p>
            <flat-pickr
              :config="configs.dateTimePickerJob"
              id="datetime-input"
              class="form-control"
              v-model="form.enddateTimeJob"
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
            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1" v-if="tr.enabled==false">
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
            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1" v-else>
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

            <!-- 2022-12-21 ADD BEGIN -->
            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
              <span class="text-success">
                <vx-tooltip color="success" text="编辑">
                  <vs-button
                    radius
                    color="success"
                    type="flat"
                    icon-pack="feather"
                    icon="icon-edit-2"
                    @click="popupActiveScheduleJob_updatefunc(tr)"
                  ></vs-button>

                  <vs-popup
                    class="holamundo"
                    title="编辑计划任务"
                    :active.sync="popupActiveScheduleJob_update"
                    background-color="rgba(0,0,0,.1)"
                  >
                  <div class="vx-row">
                    <div class="vx-col w-full">
                      <p>
                        任务名称
                        <font color="#FF0000">*</font>
                      </p>
                      <vs-input v-model="schedulejob_name" class="w-full" />
                      <br />
                    </div>
                    <div class="vx-col w-full">
                      <p>任务描述</p>
                      <vs-textarea v-model="schedulejob_description" class="w-full" />
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
                        :config="configs.dateTimePickerJob"
                        id="datetime-input"
                        class="form-control"
                        v-model="form.startdateTimeJob"
                        placeholder="选择时间"
                        style="height:40px;border-radius:5px;border:1px solid #C0C0C0;padding-left:5px;font-size:110%;color:#585858;"
                      ></flat-pickr>
                      <br />
                    </div>
                    <div class="vx-col w-full">
                      <br />
                      <p>任务结束时间</p>
                      <flat-pickr
                        :config="configs.dateTimePickerJob"
                        id="datetime-input"
                        class="form-control"
                        v-model="form.enddateTimeJob"
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
                            :vs-value="true"
                          >True</vs-radio>
                          <vs-radio
                            class="vx-col w-1/4 mt-4"
                            color="danger"
                            v-model="task_enabled"
                            :vs-value="false"
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

                  </div>
                  <br>
                    <vs-row vs-justify="center">
                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="success"
                          type="filled"
                          @click="update_schedulejob(schedulejob_id)"
                        >更新</vs-button>
                      </vs-col>

                      <vs-col v-tooltip="'col - 12'" vs-type="flex" vs-w="4">
                        <vs-button
                          color="warning"
                          type="filled"
                          @click="popupActiveScheduleJob_update=false"
                        >取消</vs-button>
                      </vs-col>
                    </vs-row>
                  </vs-popup>
                </vx-tooltip>
              </span>
            </vs-col>
            <!-- 2022-12-21 ADD END -->

            <vs-col v-tooltip="'col - 4'" vs-type="flex" vs-w="1">
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
  </div>
</template>

<script>
var padDate = function(va) {
  va = va < 10 ? "0" + va : va;
  return va;
};

import { FormWizard, TabContent } from "vue-form-wizard";
import "vue-form-wizard/dist/vue-form-wizard.min.css";
import vSelect from "vue-select";

import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import "flatpickr/dist/flatpickr.min.css";

export default {
  data() {
    return {
      schedulejobsList: [],
      //url: this.GLOBAL.baseURL,
      knowledgeBaseSearchQuery: "",
      popupActive_schedulejob: false,
      schedule_type: "",
      schedule_interval_input: false,
      schedule_cron_input: false,
      schedule_clocked_input: false,
      task_enabled: true,

      configs: {
        dateTimePickerJob: {
          enableTime: true,
          dateFormat: "Y-m-d H:i"
        }
      },

      form: {
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
      popupActiveScheduleJob_update: false,
      schedulejob_id: "",

      schedule_action_type: "",
      schedule_httpaction_input: false,
      schedule_mqttaction_input: false,
      select2_action: 0,
      options2_action: [],
      // 2022-12-21 ADD BEGIN
      schedulejob_name: "",
      schedulejob_description: "",

      // 2022-12-21 ADD END
    };
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
    }
  },

  filters: {
    formatDate: function(val) {
      var value = new Date(val);
      var year = value.getFullYear();
      var month = padDate(value.getMonth() + 1);
      var day = padDate(value.getDate());
      var hour = padDate(value.getHours());
      var minutes = padDate(value.getMinutes());
      //var seconds=padDate(value.getSeconds());
      return year + "-" + month + "-" + day + " " + hour + ":" + minutes;
    }
  },

  created: async function() {
    const response = await this.axios
      .get(this.GLOBAL.baseURL + "/trigger/periodtask/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    this.schedulejobsList = response.data;
  },

  methods: {
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
        .get(this.GLOBAL.baseURL + "/trigger/intervals/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.options1_interval = response.data;

      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalhttpaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action = response2.data;

      const response3 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/clocked/")
        .catch(function(error) {
          console.log(error);
          return error.response3.data;
        });
      console.log(response3);
      this.options1_clocked = response3.data;

      const response4 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/crons/")
        .catch(function(error) {
          console.log(error);
          return error.response4.data;
        });
      console.log(response4);
      this.options1_cron = response4.data;

      const response5 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalmqttaction/")
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
          expires: new Date(this.form.enddateTimeJob),
          start_time: new Date(this.form.startdateTimeJob),
          kwargs: JSON.stringify(tmp),
          owner: 1
        };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/periodtask/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.schedulejobsList.unshift(response.data);

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/periodtask/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.schedulejobsList = response2.data.reverse();

        this.popupActive_schedulejob = false;
        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、时间计划、触发动作都不能为空.',
            color:'danger'
          })
         }
    },

    async update_schedulejob(schedulejob_id){

      if (
        this.schedulejob_name &&
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
          name: this.schedulejob_name,
          task: tmp_task,
          interval: interval_tmp,
          crontab: cron_tmp,
          clocked: clocked_tmp,
          description: this.schedulejob_description,
          enabled: this.task_enabled,
          expires: new Date(this.form.enddateTimeJob),
          start_time: new Date(this.form.startdateTimeJob),
          kwargs: JSON.stringify(tmp),
        };
        const response = await this.axios
          .patch(this.GLOBAL.baseURL + "/trigger/periodtask/"+schedulejob_id+"/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.schedulejobsList.unshift(response.data);
        this.popupActiveScheduleJob_update = false;

        const response2 = await this.axios
          .get(this.GLOBAL.baseURL + "/trigger/periodtask/")
          .catch(function(error) {
            console.log(error);
            return error.response2.data;
          });
        this.schedulejobsList = response2.data;

        return true;
      }
      else{
           this.$vs.notify({
            title:'提醒：',
            text:'任务名称、时间计划、触发动作都不能为空.',
            color:'danger'
          })
         }

    },

    popupActiveScheduleJob_delfunc(tr) {
      this.popupActiveScheduleJob_del = true;
      this.schedulejob_id = tr.id;
    },

    // 2022-12-21 ADD BEGIN
    async popupActiveScheduleJob_updatefunc(tr) {
      this.popupActiveScheduleJob_update = true;
      this.schedulejob_id = tr.id;
      this.schedulejob_name = tr.name;
      this.schedulejob_description = tr.description;
      var tmp_schedule_type = "";
      if(tr.interval) {
        tmp_schedule_type = "INTERVAL";
      }
      if(tr.crontab) {
        tmp_schedule_type = "CRONS";
      }
      if(tr.clocked) {
        tmp_schedule_type = "CLOCKED";
      }
      this.schedule_type = tmp_schedule_type;
      this.select1_interval = tr.interval;
      this.select1_cron = tr.crontab;
      this.select1_clocked = tr.clocked;
      this.form.startdateTimeJob = tr.start_time;
      this.form.enddateTimeJob = tr.expires;
      this.task_enabled = tr.enabled;
      this.schedule_action_type =tr.action_type;
      this.select1_action = tr.action_id;
      this.select2_action = tr.action_id;

      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/intervals/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.options1_interval = response.data;

      const response2 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalhttpaction/")
        .catch(function(error) {
          console.log(error);
          return error.response2.data;
        });
      console.log(response2);
      this.options1_action = response2.data;

      const response3 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/clocked/")
        .catch(function(error) {
          console.log(error);
          return error.response3.data;
        });
      console.log(response3);
      this.options1_clocked = response3.data;

      const response4 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/crons/")
        .catch(function(error) {
          console.log(error);
          return error.response4.data;
        });
      console.log(response4);
      this.options1_cron = response4.data;

      const response5 = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/globalmqttaction/")
        .catch(function(error) {
          console.log(error);
          return error.response5.data;
        });
      console.log(response5);
      this.options2_action = response5.data;
    },

    // 2022-12-21 ADD END

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
          this.GLOBAL.baseURL + "/trigger/periodtask/" + tr.id + "/",
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
          this.GLOBAL.baseURL + "/trigger/periodtask/" + tr.id + "/",
          params
        )
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      if (response.status == "200") {
        this.schedulejobsList[indextr].enabled = false;
      }
    }
  },

  components: {
    "v-select": vSelect,
    FormWizard,
    TabContent,
    flatPickr
  }
};
</script>