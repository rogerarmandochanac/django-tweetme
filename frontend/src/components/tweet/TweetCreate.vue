<template>
  <div class="container">
    <div class="row mt-3">
        <div class="col">
            <h1 class="text-start">Crear Tweet</h1>
        </div>
        <div class="row">
            <div>
                <div class="card">
                    <div class="card-body">
                        <form action="" @submit="onSubmit">
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Title</label>
                                <div class="col-sm-6">
                                    <input type="text" placelholder="Title" name="title" class="form-control">
                                </div>
                            </div>
                            <div class="form-group row mt-2">
                                <label for="content" class="col-sm-2 col-form-label">Content</label>
                                <div class="col-sm-6">
                                    <textarea name="" id="" rows="3" placeholder="Content" class="form-control" v-model="form.content"></textarea>
                                </div>
                            </div>
                            <div class="row mt-3">
                                <div class="col text-start">
                                    <input type="submit" value="Crear" class="btn btn-primary">
                                    <router-link class="btn btn-danger ms-2" :to="{name:'home'}">Cancelar</router-link>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert';

export default {
    data(){
        return {
            tweetId:this.$route.params.tweetId,
            form:{
                title:"",
                content:"",
            }
        }
    },
    methods:{
        onSubmit(evt){
            evt.preventDefault()
            const path =  `http://127.0.0.1:8000/api/tweet/`
            axios.post(path, {content:this.form.content, user:1}).then((response)=>{
                this.form.content = response.data.content
                swal("Tweet creado exitosamente", "", "success")
            
            }).catch((err)=>{
                console.log(err)
            })
        },
    },
    computed(){

    }

}
</script>

<style>

</style>