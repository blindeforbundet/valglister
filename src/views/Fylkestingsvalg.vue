<template>
  <div class="fylkestingsvalg">
  <div class="header__container">
    <h1>Fylkestingsvalg</h1>  
    <ul>
      <li v-for="fylke in fylker" v-if="!selected_fylke"> 
          <router-link :to="{ name: 'fylkestingvalg', params: { fylke: fylke }}">{{fylke}}</router-link>
      </li>
    </ul>
    <!--
      <div v-for="v,k in partier">
      <button v-on:click="selected_parti=v">{{k}}</button>
      </div>
      -->
  </div>

  <div v-if="selected_fylke">

  <div class="sticky">
  <h2>Kandidater i <strong>{{selected_fylke}} </strong> <small>(<router-link :to="{ name: 'fylkestingvalg_velg_fylke' }">velg et annet fylke</router-link>)</small></h2>
    <label>Parti
    <select v-model="selected_parti">
      <option v-bind:value="undefined">Vis alle</option>
      <option v-for="v,k in partier" v-bind:value="v">
        {{k}}
      </option>
    </select>
    </label>

    <!--
    <label>Fylke
    <select v-model="selected_fylke">
    <option v-bind:value="undefined"></option>
      <option v-for="f in fylker" v-bind:value="f">
        {{f}}
      </option>
    </select>
    </label>
    -->
    <!-- <a v-on:click="selected_fylke = undefined; selected_parti = undefined" v-if="selected_fylke || selected_parti">Nullstill filter (vis alt)</a> -->
    </div>
    <div  class="content__container">
      <template v-for="l in filtered_parti">
          <p v-if="!l.stemmetillegg">{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</p>
          <p v-if="l.stemmetillegg" aria-label="Stemmetillegg"><strong>{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</strong></p>
      </template>
    </div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import json from '@/valglister/fylkestingsvalg.json'
export default {
  name: 'fylkestingvalg',
  components: {
    HelloWorld
  },
  mounted() {
    /*json.forEach((v)=>{
      this.partier[v.partinavn] = v.partikode
    })*/
    var fylker_dict = {}
    json.forEach((v)=>{
      fylker_dict[v.fylke] = true
      this.partier[v.partinavn] = v.partikode

    })
    this.fylker = [ ...Object.keys(fylker_dict)]
    this.fylker = this.fylker.sort()
    if(this.$route.params.fylke !== undefined) {
      this.selected_fylke = this.$route.params.fylke
    }
  },
  data(){
    return{
        myJson: json,
        partier: {},
        selected_parti: undefined,
        selected_fylke: undefined,
        fylker: undefined,
    }
  },
  computed: {
      filtered_parti() {
        var filtered_data = this.myJson
        if(this.selected_fylke !== undefined) {
          filtered_data = filtered_data.filter(i => i.fylke == this.selected_fylke)
        }
        if(this.selected_parti !== undefined){
          filtered_data = filtered_data.filter(i => i.partikode == this.selected_parti)

        }
        return filtered_data
    },

  }
}
</script>
