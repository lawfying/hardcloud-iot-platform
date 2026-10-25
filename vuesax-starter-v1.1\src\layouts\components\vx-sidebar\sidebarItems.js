/*=========================================================================================
  File Name: sidebarItems.js
  Description: Sidebar Items list. Add / Remove menu items from here.
  Strucutre:
  				url 		=> router path
  				name 		=> name to display in sidebar
  				slug 		=> router path name
  				icon 		=> Feather Icon component/icon name
  				tag 		=> text to display on badge
  				tagColor 	=> class to apply on badge element
  				i18n 		=> Internationalization
  				submenu 	=> submenu of current item (current item will become dropdown )
  							NOTE: Submenu don't have any icon(you can add icon if u want to display)
  				isDisabled 	=> disable sidebar item/group
  ----------------------------------------------------------------------------------------
  Item Name: Vuesax Admin - VueJS Dashboard Admin Template
  Version: 1.1
  Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/


export default [
    {
		url: "/dashboard",
		name: "仪表盘",
		slug: "dashboard",
		icon: "HomeIcon",
	},

	{
		header: "设备管理",
	},
	{
		url: "/devices/templates",
		name: "设备模板",
		slug: "devicetemplates",
		icon: "CopyIcon",
	},
	{
		url: "/devices/lists",
		name: "设备列表",
		slug: "deviceslists",
		icon: "PackageIcon",
	},

	{
		url: "/devices/subscribe",
		name: "MQTT-云端订阅",
		slug: "subscribe",
		icon: "ClockIcon",
	},
	{
		url: "/devices/holders",
		name: "设备持有者",
		slug: "holders",
		icon: "UsersIcon",
	},
	{
		header: "应用场景管理",
	},
	{
		url: "/scenarios/scenarios",
		name: "应用场景",
		slug: "scenarios",
		icon: "MapIcon",
	},
	// {
	// 	url: "/page2",
	// 	name: "拓扑结构",
	// 	slug: "page2",
	// 	icon: "MenuIcon",
	// },
	// {
	// 	url: "/page2",
	// 	name: "数据监测",
	// 	slug: "page2",
	// 	icon: "MonitorIcon",
	// },
	{
		url: "/scenarios/holders",
		name: "场景持有者",
		slug: "scenario holders",
		icon: "UsersIcon",
	},

	{
		header: "任务联动管理",
	},

	{
		url: "/triggers/schedules",
		name: "时间计划",
		slug: "schedules",
		icon: "ClockIcon",
	},

	{
		url: "/triggers/actions",
		name: "执行动作",
		slug: "actions",
		icon: "SendIcon",
	},


	{
		url: "/triggers/schedulejobs",
		name: "计划任务设置",
		slug: "schedulejobs",
		icon: "CheckSquareIcon",
	},
	
	{
		url: "/triggers/triggerjobs",
		name: "触发任务设置",
		slug: "triggerjobs",
		icon: "BellIcon",
	},
	{
		header: "文档及支持",
	},
	{
		url: "/swaggerui",
		name: "Swagger UI接口",
		slug: "docs",
		icon: "BookOpenIcon",
	},
	// {
	// 	url: "/redocui",
	// 	name: "Redoc UI接口",
	// 	slug: "redoc",
	// 	icon: "LifeBuoyIcon",
	// },

	{
		header: "用户管理",
	},
	{
		url: '/pages/myprofile',
		name: "个人中心",
		slug: "httpapi",
		icon: "UserIcon",
	},
	{
		url: "/pages/login",
		name: "退出",
		slug: "home",
		icon: "LogOutIcon",
	},



]