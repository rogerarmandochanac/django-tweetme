<template>
  <div class="container">
    <div class="row mt-3">
        <div class="col">
            <h1>TweetMe</h1>
        </div>
        <div class="row">
            <div class="col-2" id="navbar-container">
                <TweetNavbar></TweetNavbar>
            </div>
            <div class="col-8 mt-4">
                <router-link class="btn btn-primary mb-3 ms-start" :to="{name:'tweet-create'}">Crear tweet</router-link>
                <div v-for="tweet in tweets" :key="tweet.id" class="row">
                    <div class="col-4">
                        <img src="" alt="Imagen de perfil">
                    </div>
                    <div class="col-8">
                        <div class="card mb-3 p-3">
                            <h5 class="text-start">{{ tweet.content }}</h5>
                            <div class="d-flex">
                                <small class="text-start">{{ tweet.timestamp }}</small>
                                <small class="ms-3 btn-edit"><router-link :to="{name:'tweet-edit', params:{tweetId:tweet.pk}}">Edit</router-link></small>
                                <small class="ms-3 btn-delete"><router-link :to="{name:'tweet-delete', params:{tweetId:tweet.pk}}">Delete</router-link></small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-2"></div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TweetNavbar from './TweetNavbar.vue';


export default {
    data(){
        return {
            tweets:[]
        }
    },
    methods:{
        getTweets(){
            const path = 'http://127.0.0.1:8000/api/tweet/';
            axios.get(path).then((response)=>{
                this.tweets = response.data
            }).catch((err)=>{
                console.log(err)
            })
        }
    },
    created(){
        this.getTweets()
    },
    components:{
        TweetNavbar,
    }
}
</script>

<style>
    #navbar-container ul a{
        text-align: left;
        text-decoration: none;
        list-style: none;
        text-transform: uppercase;
        color:black;
    }

    .btn-delete, .btn-edit{
        cursor: pointer;
    }

    .btn-delete:hover{
        color:red;
    }

    .btn-edit:hover{
        color:darkgreen;
    }
</style>