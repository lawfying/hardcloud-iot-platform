<template>
  <div class="mt-5">
    <vs-tabs vs-alignment="fixed">
      <vs-tab vs-label="间隔时间">
        <div>
          <div class="flex flex-wrap">
            <vs-row>
              <vs-col
                vs-offset="2"
                v-tooltip="'col - 8'"
                vs-type="flex"
                vs-justify="center"
                vs-align="center"
                vs-w="8"
              >
                <vx-card class="overlay-card overflow-hidden">
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
                      <div class="centerx">
                        <span>间隔：</span>
                      </div>
                    </vs-col>
                    <vs-col v-tooltip="'col - 2'" vs-type="flex" vs-w="2">
                      <vs-input-number color="success" min="1" v-model="interval_num" />
                    </vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
                      <div class="centerx">
                        <span>周期：</span>
                      </div>
                    </vs-col>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="3">
                      <vs-select autocomplete class="selectExample" v-model="select1">
                        <vs-select-item
                          :key="index"
                          :value="item.value"
                          :text="item.text"
                          v-for="(item,index) in options1"
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
                  <vs-divider />
                  <br />
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
                </vx-card>
              </vs-col>
            </vs-row>
          </div>
        </div>
      </vs-tab>
      <vs-tab vs-label="定时时间" @click="clockedinit()">
        <div>
          <div class="flex flex-wrap">
            <vs-row>
              <vs-col
                vs-offset="2"
                v-tooltip="'col - 8'"
                vs-type="flex"
                vs-justify="center"
                vs-align="center"
                vs-w="8"
              >
                <vx-card class="overlay-card overflow-hidden">
                  <vs-row>
                    <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="1">
                      <div class="centerx">
                        <span>定时：</span>
                      </div>
                    </vs-col>
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

                    <vs-col
                      vs-type="flex"
                      vs-justify="center"
                      vs-align="center"
                      vs-w="4"
                      style="padding-bottom:2px;"
                    >
                      <!-- <feather-icon icon="PlayCircleIcon" svgClasses="text-grey"></feather-icon>
                      <span style="padding-left:10px;">启用</span> -->
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
                vs-offset="2"
                v-tooltip="'col - 8'"
                vs-type="flex"
                vs-justify="center"
                vs-align="center"
                vs-w="8"
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
</template>

<script>
var padDate = function(va) {
  va = va < 10 ? "0" + va : va;
  return va;
};

import vSelect from "vue-select";

import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import "flatpickr/dist/flatpickr.min.css";

export default {
  data() {
    return {
      interval_num: 1,
      select1: "MINUTES",
      options1: [
        { text: "DAYS", value: "DAYS" },
        { text: "HOURS", value: "HOURS" },
        { text: "MINUTES", value: "MINUTES" },
        { text: "SECONDS", value: "SECONDS" },
        { text: "MICROSECONDS", value: "MICROSECONDS" }
      ],
      intervalList: [],
      popupActiveInterval_update: false,
      interval_every: "",
      select1_period: "",
      tmp_interval_id: "",

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
      popupActiveCrons_update: false
    };
  },
  mounted: async function() {
    const response = await this.axios
      .get(this.GLOBAL.baseURL + "/trigger/intervals/")
      .catch(function(error) {
        console.log(error);
        return error.response.data;
      });
    console.log(response);
    this.intervalList = response.data;
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

  methods: {
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

    async addinterval() {
      var params = {
        every: this.interval_num,
        period: this.select1.toLowerCase(),
        owner: 1
      };
      const response = await this.axios
        .post(this.GLOBAL.baseURL + "/trigger/intervals/", params)
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      this.intervalList.unshift(response.data);
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
          this.GLOBAL.baseURL + "/trigger/intervals/" + tmp_interval_id + "/",
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
    async addclocked() {
      if (this.form.dateTime != null) {
        var params = { clocked_time: new Date(this.form.dateTime), owner: 1 };
        const response = await this.axios
          .post(this.GLOBAL.baseURL + "/trigger/clocked/", params)
          .catch(function(error) {
            console.log(error);
            return error.response.data;
          });
        this.clockedList.unshift(response.data);
      }
      return true;
    },

    async clockedinit() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/clocked/")
        .catch(function(error) {
          console.log(error);
          return error.response.data;
        });
      console.log(response);
      this.clockedList = response.data;
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
          this.GLOBAL.baseURL + "/trigger/clocked/" + tmp_clocked_id + "/",
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

    popupActiveInterval_delfunc(tag) {
      this.tmp_interval_id = tag.id;
      this.popupActiveInterval_del = true;
    },
    async delinterval(tmp_interval_id) {
      var url =
        this.GLOBAL.baseURL + "/trigger/intervals_top/" + tmp_interval_id + "/";
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

    async cronsinit() {
      const response = await this.axios
        .get(this.GLOBAL.baseURL + "/trigger/crons/")
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
        owner: 1
      };
      const response = await this.axios
        .post(this.GLOBAL.baseURL + "/trigger/crons/", params)
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
          this.GLOBAL.baseURL + "/trigger/crons/" + tmp_crons_id + "/",
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
    }
  },

  components: {
    "v-select": vSelect,
    flatPickr
  }
};
</script>
		