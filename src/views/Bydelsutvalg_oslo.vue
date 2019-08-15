<template>
  <div class="home">
  <h1>Bydelsutvalg oslo</h1>

    <label>Parti
    <select v-model="selected_parti">
      <option v-bind:value="undefined">Vis alle</option>
      <option v-for="v,k in partier" v-bind:value="v">
        {{k}}
      </option>
    </select>
    </label>

    <label>Bydel
    <select v-model="selected_bydel">
    <option v-bind:value="undefined">Vis alle</option>
      <option v-for="f in bydeler" v-bind:value="f">
        {{f}}
      </option>
    </select>
    </label>

        <div v-for="l in filtered_parti">
    <!-- {{l}} -->
        <p v-if="!l.stemmetillegg">{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</p>
        <p v-if="l.stemmetillegg" aria-label="Stemmetillegg"><strong>{{l.kandidatnr}} {{l.fylke}} {{l.navn}} ({{l.kjønn }}, f. {{l.fødselsår }}) {{l.partinavn}}</strong></p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import json from '@/valglister/valg_bydelsutvalg_oslo.json'
export default {
  name: 'bydelsutvalg_oslo',
  components: {

  },
  created() {
    /*json.forEach((v)=>{
      this.partier[v.partinavn] = v.partikode
    })*/

    var bydel_dict = {}
    json.forEach((v)=>{
      bydel_dict[v.bydel] = true
      this.partier[v.partinavn] = v.partikode
      
    })
    this.bydeler = [ ...Object.keys(bydel_dict)]
    this.bydeler = this.bydeler.sort()
  },
  data(){
    return{
        myJson: json,
        partier: {},
        selected_parti: undefined,
        selected_bydel: undefined,
        bydeler: undefined
    }
  },
  computed: {
      filtered_parti() {
        var filtered_data = this.myJson
        if(this.selected_bydel !== undefined) {
          filtered_data = filtered_data.filter(i => i.bydel == this.selected_bydel)
        }
        if(this.selected_parti !== undefined){
          filtered_data = filtered_data.filter(i => i.partikode == this.selected_parti)

        }
        return filtered_data
    },

  }
}
</script>
