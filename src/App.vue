<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/fylkestingsvalg">Fylkestingsvalg</router-link> |
      <router-link to="/kommunestyrevalg">Kommunestyrevalg</router-link> |
      <router-link to="/bydelsutvalg_oslo">Bydelsutvalg Oslo</router-link>
      
      
    </div>
    <router-view :key="$route.fullPath"/>
  </div>
</template>

<style>
html {
  overflow-y: scroll;
}
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
label {
    display: block;
    font-weight: bold;
    color: #000;
    margin-bottom: 7.5px;
    cursor: pointer;

}
select {
    display: block;
    padding: 6px 15px 5px 30px;
    margin: 0 15px 30px 0;
    /*width: 100%;*/
    min-width: 140px;
    /*background: url(../graphics/png/sprite.png) no-repeat right center;*/
    background: none,#fff url(assets/sprite.svg) no-repeat;
    background-position: left center;
    background-color: white;
    color: #000;
    border: 3px solid #f29400;
    font-size: inherit;
    line-height: inherit;
    font-family: inherit;
    font-weight: inherit;
    cursor: pointer;
    -webkit-appearance: none;
    -moz-appearance: none;
    -o-appearance: none;
    appearance: none;
    -webkit-border-radius: 0;
    border-radius: 0;

}

.sticky {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  background-color: whitesmoke;
  padding: 5px 20px;
  border-radius: 25px;

}
</style>
