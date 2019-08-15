<template>
  <div class="fylkestingsvalg">
  <h1>Fylkestingsvalg</h1>
  <!--
    <div v-for="v,k in partier">
    <button v-on:click="selected_parti=v">{{k}}</button>
    </div>
    -->
    <label>Parti
    <select v-model="selected_parti">
      <option v-bind:value="undefined"></option>
      <option v-for="v,k in partier" v-bind:value="v">
        {{k}}
      </option>
    </select>
    </label>

    <label>Fylke
    <select v-model="selected_fylke">
    <option v-bind:value="undefined"></option>
      <option v-for="f in fylker" v-bind:value="f">
        {{f}}
      </option>
    </select>
    </label>
    <a v-on:click="selected_fylke = undefined; selected_parti = undefined" v-if="selected_fylke || selected_parti">Nullstill filter (vis alt)</a>

    <div v-for="l in filtered_parti">
    <!-- {{l}} -->
    <p>{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }} {{l.fødselsår }}) {{l.partinavn}} (partikode: {{l.partikode}}) {{l.stemmetillegg}}</p>
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
