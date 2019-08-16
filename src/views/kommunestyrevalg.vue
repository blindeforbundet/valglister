<template>
  <div class="home" v-cloak>
  <div class="header__container">
    <h1>Kommunestyrevalg</h1>
    <ul>
      <li v-for="fylke in fylker" v-bind:key="fylke" v-if="!selected_fylke"> 
        <router-link :to="{ name: 'kommunestyrevalg', params: { fylke: fylke }}">{{fylke}}</router-link>
      </li>
    </ul>
  </div>

  <div v-if="selected_fylke">
  
  <div  class="sticky">
    <h2>Kandidater i <strong>{{selected_fylke}} </strong> <small>(<router-link :to="{ name: 'kommunestyrevalg_velg_fylke' }">velg et annet fylke</router-link>)</small></h2>
    <!--
    <label>Fylke
    <select v-model="selected_fylke">
    
      <option v-for="f in fylker" v-bind:value="f">
        {{f}}
      </option>
    </select>
    </label>
    -->
    <label>Kommune
      <select v-model="selected_kommune">
        <option v-bind:value="undefined">Vis alle</option>
        <option v-for="v,k in filtered_kommuner" v-bind:value="v.kommunenr">
          {{v.kommunenavn}}
        </option>
      </select>
    </label>

    <label>Parti
      <select v-model="selected_parti">
        <option v-bind:value="undefined">Vis alle</option>
        <option v-for="v,k in partier" v-bind:value="k">
          {{v}}
        </option>
      </select>
    </label>
  </div>
    

    <div v-if="render" class="content__container">
        <template v-for="l in filtered_parti">
          <p v-if="!l.stemmetillegg">{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</p>
          <p v-if="l.stemmetillegg" aria-label="Stemmetillegg"><strong>{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</strong> <span class="screenreader">Stemmetillegg</span></p>
        </template>
        <p v-if="filtered_parti.length < 1">
        ingen kandidater for <strong>{{partier[selected_parti]}}</strong> i <strong>{{selected_fylke}}</strong>
        </p>
    </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import json from '@/valglister/komunestyrevalg.json'
export default {
  name: 'kommunestyrevalg',
  components: {

  },
  created() {
    /*json.forEach((v)=>{
      this.partier[v.partinavn] = v.partikode
    })*/
    this.selected_fylke = this.$route.params.fylke
    if(this.$route.params.fylke !== undefined) {
      this.selected_fylke = this.$route.params.fylke
    }
    var fylker_dict = {}

    json.forEach((v)=>{
      fylker_dict[v.fylke] = true
      //this.partier[v.partinavn] = v.partikode
      this.partier[v.partikode] = v.partinavn
      this.kommuner[v.kommunenr] = {'kommunenavn': v.kommune, 'kommunenr': v.kommunenr, 'fylke': v.fylke }
      })
    this.fylker = [ ...Object.keys(fylker_dict)]
    this.fylker = this.fylker.sort()
  },
  data(){
    return{
        myJson: json,
        partier: {},
        selected_parti: undefined,
        selected_fylke: undefined,
        selected_kommune: undefined,
        fylker: undefined,
        kommuner: {},
        render: true
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
        if(this.selected_kommune  !== undefined){
          filtered_data = filtered_data.filter(i => i.kommunenr == this.selected_kommune)
        }
        return filtered_data
    },
    filtered_kommuner() {
      var filtered = []
      Object.keys(this.kommuner).forEach(key => {
        if(this.kommuner[key].fylke == this.selected_fylke) {
        filtered.push(this.kommuner[key])
        }
      });
      
      return filtered.sort((a,b) => (a.kommunenavn > b.kommunenavn) ? 1 : ((b.kommunenavn > a.kommunenavn) ? -1 : 0))
    }

  },
  methods:{
    prepare_data() {
      
    }
  },
}
</script>
