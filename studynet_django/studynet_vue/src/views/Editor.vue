<template>
    <div>
      <div class="header">Coba IDE</div>
      <div class="control-panel">
        Select Language:
        &nbsp; &nbsp;
        <select v-model="selectedLanguage" class="languages" title="Change language" @change="changeLanguage">
          <option value="c">C</option>
          <option value="cpp">C++</option>
          <option value="php">PHP</option>
          <option value="python">Python</option>
          <option value="node">Node JS</option>
        </select>
      </div>
      <div class="container">
        <div class="editor-container">
          <div class="editor" id="editor" ref="editor"></div>
          <div class="button-container">
            <button class="btn" @click="executeCode">Run</button>
          </div>
        </div>
        <div class="output-container">
          <pre class="output ace_dark ace_monokai ace_hidpi ace_editor ace_focus" ref="output"></pre>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        selectedLanguage: "c",
        editor: null
      };
    },
    mounted() {
      this.editor = ace.edit(this.$refs.editor);
      this.editor.setTheme("ace/theme/monokai");
      this.editor.session.setMode("ace/mode/c_cpp");
    },
    methods: {
      changeLanguage() {
        const language = this.selectedLanguage;
        if (language === "c" || language === "cpp") {
          this.editor.session.setMode("ace/mode/c_cpp");
        } else if (language === "php") {
          this.editor.session.setMode("ace/mode/php");
        } else if (language === "python") {
          this.editor.session.setMode("ace/mode/python");
        } else if (language === "node") {
          this.editor.session.setMode("ace/mode/javascript");
        }
      },
      executeCode() {
        const language = this.selectedLanguage;
        const code = this.editor.getSession().getValue();
  
        axios
          .post("/ide/app/compiler", { language, code })
          .then(response => {
            this.$refs.output.textContent = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>
  