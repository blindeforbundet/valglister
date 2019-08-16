<template>
  <div id="app">
    <div id="nav" role="navigation">
      <router-link to="/fylkestingsvalg">Fylkestingsvalg</router-link>
      <router-link to="/kommunestyrevalg">Kommunestyrevalg</router-link>
      <router-link to="/bydelsutvalg_oslo">Bydelsutvalg Oslo</router-link>
      <router-link to="/">Om denne tjenesten</router-link>
    </div>
    <router-view :key="$route.fullPath"/>
  </div>
</template>

<style>
@font-face {
    font-family: "TheSans";
    src: url("assets/TheSans_LT_500_.woff") format('woff');
}

html {
  overflow-y: scroll;
}
body {
  font-family: 'TheSans', Helvetica, Arial, sans-serif;
  font-size: 1.4rem;
  margin: 0;
}
#app {
  
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
    max-width: 100%;
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

ul {
  padding: 0;
}

.sticky {
  /*position: -webkit-sticky;
  position: sticky;
  top: 0;*/
  background-color: whitesmoke;
  padding: 5px 20px;
  border-radius: 25px;

}

#nav>a {
  color: black;
    text-decoration: none;
    border-bottom: 4px dotted black;
    display: inline-block;
    margin: 10px;
}
#nav a:hover {
    text-decoration: none;
    border-bottom: 4px solid black;
}

@media only screen and (max-width: 790px) {
  #nav>a { 
    display: block;
  }
  h1 {
    font-size: 1.5em;
  }
} 



a {
    color: #c60c30;
    text-decoration: none;
    /*border-bottom: 1px dotted #c60c30; */
    
    text-decoration: underline;
    text-decoration-style: dotted;

}
a:hover {
    color: #c60c30;
    text-decoration: none;
    /*border-bottom: 1px dotted #c60c30; */
    
    text-decoration: underline;
    text-decoration-style: solid;

}

.screenreader {
    position: absolute !important; /* Outside the DOM flow */
    height: 1px; width: 1px; /* Nearly collapsed */
    overflow: hidden;
    clip: rect(1px 1px 1px 1px); /* IE 7+ only support clip without commas */
    clip: rect(1px, 1px, 1px, 1px); /* All other browsers */
}

.header__container {
  margin: 0 20px;
}

.content__container {
  margin: 0 20px;

}
</style>
