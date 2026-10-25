/*=========================================================================================
  File Name: router.js
  Description: Routes for vue-router. Lazy loading is enabled.
  Object Strucutre:
  					path => router path
  					name => router name
  					component(lazy loading) => component to load
  ----------------------------------------------------------------------------------------
  Item Name: Vuesax Admin - VueJS Dashboard Admin Template
  Version: 1.1
  Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/


import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
	base: process.env.BASE_URL,
	routes: [

		{
	// =============================================================================
	// MAIN LAYOUT ROUTES
	// =============================================================================
			path: '',
			component: () => import('./layouts/main/Main.vue'),
			children: [
		// =============================================================================
		// Theme Routes
		// =============================================================================

				{
					path: '/dashboard',
					name: 'dashboard',
					component: () => import('./views/DashboardAnalytics.vue'),
					meta: { requiresAuth: true },
				},

				{
					path: '/devices/templates',
					name: 'templates',
					component: () => import('@/views/devices/Templates.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备管理' },
							{ title: '设备模板', active: true },
						],
						pageTitle: '设备模板',
						requiresAuth: true
					},
				},

				{
					path: '/devices/template-details',
					name: 'templateDetails',
					component: () => import('@/views/devices/TemplateDetails.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备模板',url:'/devices/templates' },
							{ title: '模板详情', active: true },
						],
						pageTitle: '模板详情',
						requiresAuth: true
					},
				},

				{
					path: '/devices/device-details',
					name: 'deviceDetails',
					component: () => import('@/views/devices/DeviceDetails.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备列表',url:'/devices/lists' },
							{ title: '设备详情', active: true },
						],
						pageTitle: '设备详情',
						requiresAuth: true
					},
				},

				{
					path: '/devices/lists',
					name: 'devicesLists',
					component: () => import('@/views/devices/Devices.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备管理' },
							{ title: '设备列表', active: true },
						],
						pageTitle: '设备列表',
						requiresAuth: true
					},
				},

				{
					path: '/devices/subscribe',
					name: 'devicesSubscribe',
					component: () => import('@/views/devices/SubscribeDevices.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备管理' },
							{ title: '订阅设备', active: true },
						],
						pageTitle: '订阅设备',
						requiresAuth: true
					},
				},

				{
					path: '/devices/holders',
					name: 'deviceHolders',
					component: () => import('@/views/devices/DeviceHolders.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '设备管理' },
							{ title: '持有者', active: true },
						],
						pageTitle: '设备持有者',
						requiresAuth: true
					},
				},

				{
					path: '/scenarios/scenarios',
					name: 'scenarios',
					component: () => import('@/views/scenarios/Scenarios.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '应用场景' },
							{ title: '应用场景', active: true },
						],
						pageTitle: '应用场景',
						requiresAuth: true
					},
				},

				{
					path: '/scenarios/scenario-details',
					name: 'scenarioDetails',
					component: () => import('@/views/scenarios/ScenarioDetails.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '应用场景',url:'/scenarios/scenarios' },
							{ title: '应用场景详情', active: true },
						],
						pageTitle: '应用场景详情',
						requiresAuth: true
					},
				},

				{
					path: '/scenarios/collection-details',
					name: 'collectionDetails',
					component: () => import('@/views/scenarios/CollectionDetails.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '应用场景',url:'/scenarios/scenarios' },
							{ title: '场景详情',url:'/scenarios/scenario-details' },
							{ title: '设备组合详情', active: true },
						],
						pageTitle: '设备详情',
						requiresAuth: true
					},
				},

				{
					path: '/scenarios/holders',
					name: 'scenarioHolders',
					component: () => import('@/views/scenarios/ScenarioHolders.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '场景管理' },
							{ title: '持有者', active: true },
						],
						pageTitle: '场景持有者',
						requiresAuth: true
					},
				},

				{
					path: '/triggers/schedules',
					name: 'schedules',
					component: () => import('@/views/triggers/Schedules.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '任务联动' },
							{ title: '时间计划', active: true },
						],
						pageTitle: '时间计划',
						requiresAuth: true
					},
				},

				{
					path: '/triggers/actions',
					name: 'actions',
					component: () => import('@/views/triggers/Actions.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '任务联动' },
							{ title: '执行动作', active: true },
						],
						pageTitle: '执行动作',
						requiresAuth: true
					},
				},

				{
					path: '/triggers/schedulejobs',
					name: 'schedulejobs',
					component: () => import('@/views/triggers/ScheduleJobs.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '任务联动' },
							{ title: '计划任务', active: true },
						],
						pageTitle: '计划任务',
						requiresAuth: true
					},
				},

				{
					path: '/triggers/triggerjobs',
					name: 'triggerjobs',
					component: () => import('@/views/triggers/triggerJobs.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '任务联动' },
							{ title: '触发任务', active: true },
						],
						pageTitle: '触发任务',
						requiresAuth: true
					},
				},

				{
					path: '/pages/myprofile',
					name: 'myprofile',
					component: () => import('@/views/pages/MyProfile.vue'),
					meta: {
						breadcrumb: [
							{ title: 'Home', url: '/' },
							{ title: '用户中心' },
							{ title: '我的信息', active: true },
						],
						pageTitle: '我的信息',
						requiresAuth: true
					},
				},

				// {
				// 	path: '/redocui',
				// 	name: 'redoc',
				// 	component: () => import('./views/Redocui.vue'),
				// 	meta: { requiresAuth: true },
				// },
				{
					path: '/swaggerui',
					name: 'swagger',
					component: () => import('./views/Swaggerui.vue'),
					meta: { requiresAuth: true },
				},
			],
			meta: { requiresAuth: true },
		},
	// =============================================================================
	// FULL PAGE LAYOUTS
	// =============================================================================
		{
			path: '',
			component: () => import('@/layouts/full-page/FullPage.vue'),
			children: [
		// =============================================================================
		// PAGES
		// =============================================================================
				{
					path: '/pages/login',
					name: 'pageLogin',
					component: () => import('@/views/pages/Login.vue')
				},
				{
					path: '/pages/register',
					name: 'pageRegister',
					component: () => import('@/views/pages/Register.vue')
				},
				{
					path: '/pages/error-404',
					name: 'pageError404',
					component: () => import('@/views/pages/Error404.vue')
				},
			]
		},
		// Redirect to 404 page, if no match found
		{
			path: '*',
			redirect: '/pages/error-404'
		}
	],
})