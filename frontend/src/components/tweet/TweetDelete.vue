<template>
    <div>
        <h1>
        Esta seguro que desea eliminar el siguiente elemento:
        </h1>
        <p>{{ content }}</p>
        <button class="btn btn-danger" @click="deteleTweet">Eliminar</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return {
            tweetId:this.$route.params.tweetId,
            content:""
        }
    },

    methods:{
        getTweet(){
            const path = `http://127.0.0.1:8000/api/tweet/${this.tweetId}/`
            axios.get(path).then((response)=>{
                this.content = response.data.content
            })
        },

        deteleTweet(){
            const path = `http://127.0.0.1:8000/api/tweet/${this.tweetId}/`
            axios.delete(path).then(()=>{
                location.href = '/'
            }).catch((err)=>{console.log(err)})
        }
    },
    created(){
        this.getTweet()
    }

}
</script>

<style>

</style>