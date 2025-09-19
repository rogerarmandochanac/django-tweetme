import { createRouter, createWebHistory } from 'vue-router'
import TweetList from '../components/tweet/TweetList.vue'
import TweetEdit from '@/components/tweet/TweetEdit.vue'
import TweetDelete from '@/components/tweet/TweetDelete.vue'
import TweetCreate from '@/components/tweet/TweetCreate.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: TweetList
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/tweet/edit/:tweetId',
    name:'tweet-edit',
    component:TweetEdit
  },

  {
    path:'/tweet/delete/:tweetId',
    name:'tweet-delete',
    component:TweetDelete
  },

    {
    path:'/tweet/create/',
    name:'tweet-create',
    component:TweetCreate
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
