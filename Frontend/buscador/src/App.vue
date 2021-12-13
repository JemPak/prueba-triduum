<template>
  <div class="container">
    <header>
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia-logo_%28inverse%29.png"
        alt="Wikipedia Logo"
        width="300"
        class="header__image"
      />
      <h1 class="header__title">BUSCADOR LATINO</h1>
      <div class="header__search-bar">
        <input
          v-model="word"
          aria-label="¿Qué deseas Buscar?"
          type="text"
          class="search-bar__input"
          placeholder="¿Qué deseas Buscar?"
          autofocus
          required
        />
        <button
          v-on:click="search"
          type="button"
          class="search-bar__button"
          aria-label="search"
        >
          <!-- inline SVG search icon -->
          <svg
            version="1.1"
            id="Layer_1"
            x="0px"
            y="0px"
            width="15px"
            height="15px"
            viewBox="0 0 25 25"
            enable-background="new 0 0 25 25"
            xml:space="preserve"
          >
            <path
              fill="#C0C0C0"
              d="M23.888,21.266l-5.629-5.628c1.1-1.604,1.742-3.545,1.742-5.637C20.001,4.478,15.526,0,10,0
                            C4.478,0,0,4.478,0,10.001S4.478,20,10,20c2.204,0,4.233-0.721,5.885-1.927l5.598,5.597c0.717,0.718,1.838,0.761,2.5,0.097
                            C24.647,23.104,24.604,21.983,23.888,21.266z M10,16.748c-3.728,0-6.749-3.021-6.749-6.747c0-3.728,3.021-6.749,6.749-6.749c3.729,0,6.749,3.021,6.749,6.749C16.749,13.728,13.729,16.748,10,16.748z"
            />
          </svg>
        </button>
      </div>
    </header>
  </div>

  <div class="results">
    <div v-if="!valid" class="results__error">
      <p> {{errorResponse}}</p>
    </div>

    <div v-if="valid"  class="results__items">
      <div v-for="results in data" :key="results.title">
        <div class="results__item">
              <a :href="`https://en.wikipedia.org/?curid=${results.pageid}`" target="_blank" class="card animated bounceInUp">
                  <h2 class="results__item__title">{{results.title}}</h2>
                  <p v-html="results.snippet" class="results__item__snipet"></p>
                  <p class="results__item__pageid"><strong>Página:</strong> {{results.pageid}}</p>
              </a>
        </div>
      </div>
    </div>

  </div>
  <router-view/>
</template>

<script>
import axios from "axios";

export default {
  name: "Search",
  data: function(){
    return {
      word: "",
      valid: true,
      errorResponse: "",
      data: [],
    }
  },
  methods: {
    search: async function(){
      /**
       * Async await function to get Query with word 
       * sent by user, first validate not null value, then
       * get Query with AXIOS and render variables
       */
      if (this.word == ""){
        this.valid = false; 
        return null
      } 
      let url = "https://en.wikipedia.org/w/api.php?"; 

      let params = {
        origin: '*',
        action: "query",
        format: "json",
        list: "search",
        srsearch: this.word
      };
      url = url + "?origin=*";
      // order url with params required by Wikipedia API
      Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});
      // axios Query, use await because server need wait response to wikipedia
      await axios.get(
        url
      ).then((response) => {
        // response Query
        if (response.data.query.search.length == 0){
          this.errorResponse = "la información buscada no existe";
          this.valid = false
          return null
        }
        this.valid = true
        this.data = response.data.query.search
      }).catch((error) => {
        // catch error by user
        this.valid = false
        this.errorResponse = "ocurrio un error en la consulta";
        return null
      });
    }
  },
};
</script>


<style>
* {
    box-sizing: border-box;
    font-family: 'Raleway', sans-serif;
}

body {
    font-size: 16px;
}

a {
    color: inherit;
    text-decoration: none;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
    margin-top: 3rem;
}

.header__image {
    max-width: 300px;
    width: 100%;
}

.header__title {
    font-family: 'Zilla Slab', serif;
    font-weight: 500;
    font-size: 2.5rem;
}

.header__search-bar {
    display: flex;
    justify-content: space-between;
    width: 320px;
    padding: 5px;
    border: 1px solid #f4f4f4;
    margin: 40px auto;
    box-shadow: 0px 2px 4px #dfdfdf;
}

.header__search-bar:hover {
    box-shadow: 0px 3px 5px #c0c0c0;
}

.search-bar__input {
    font-size: 1rem;
    width: 85%;
    border: none;
    padding: 0.5rem;
    outline-color: #1c1b1b;
}

.search-bar__button {
    padding: 0.75rem;
    border: none;
    outline-color: #1c1b1b;
    background-color: #fcfcfc;
    cursor: pointer;
}
.search-bar__input:disabled,
.search-bar__button:disabled {
    cursor: not-allowed;
}

.results {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.results__items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.results__error {
    color: #ef0000;
}

.results__item {
    background: #fff;
    border-radius: 2px;
    display: inline-block;
    height: 275px;
    margin: 1rem;
    /* position: relative; */
    width: 300px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    cursor: pointer;
    overflow: hidden;
}
.results__item:hover {
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
.results__item__title {
    font-family: 'Zilla Slab', serif;
    font-weight: 500;
    margin: 20px;
}
.results__item__snippet {
    margin: 0 20px;
    padding-bottom: 20px;
}
.results__item__pageid {
    position: relative;
    bottom: -5%;
    padding-bottom: 20px;
}
</style>
