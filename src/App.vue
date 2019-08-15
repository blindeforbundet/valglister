<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/fylkestingsvalg">Fylkestingsvalg</router-link> |
      <router-link to="/kommunestyrevalg">Kommunestyrevalg</router-link> |
      <router-link to="/bydelsutvalg_oslo">Bydelsutvalg Oslo</router-link>
      
      
    </div>
    <router-view/>
  </div>
</template>

<style>
body {
  font-size: 20px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  max-width: 960px;
  margin: 0 auto;

}
</style>
