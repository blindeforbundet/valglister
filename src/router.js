import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Fylkestingsvalg from './views/Fylkestingsvalg.vue'
import Kommunestyrevalg from './views/Kommunestyrevalg.vue'
import Bydelsutvalg_oslo from './views/Bydelsutvalg_oslo.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/fylkestingsvalg',
      name: 'fylkestingvalg_velg_fylke',
      component: Fylkestingsvalg
    },
    {
      path: '/fylkestingsvalg/:fylke',
      name: 'fylkestingvalg',
      component: Fylkestingsvalg
    },
    {
      path: '/kommunestyrevalg',
      name: 'kommunestyrevalg_velg_fylke',
      component: Kommunestyrevalg
    },
    {
      path: '/kommunestyrevalg/:fylke',
      name: 'kommunestyrevalg',
      component: Kommunestyrevalg
    },
    {
      path: '/bydelsutvalg_oslo',
      name: 'bydelsutvalg_oslo',
      component: Bydelsutvalg_oslo
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
