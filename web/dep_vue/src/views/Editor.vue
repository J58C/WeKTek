<template>
  <div>
    <div class="header">Coba IDE</div>
    <div class="control-panel">
      Select Language:
      &nbsp; &nbsp;
      <select title="IDE" v-model="selectedLanguage" class="languages" @change="changeLanguage">
        <option value="c">C</option>
        <option value="cpp">C++</option>
        <option value="php">PHP</option>
        <option value="python">Python</option>
        <option value="node">Node JS</option>
      </select>
    </div>
    <div class="editor" id="editor"></div>

    <div class="output">{{ output }}</div>

    <div class="button-container">
      <button class="btn" @click="executeCode">Run</button>
    </div>
  </div>
</template>

<script>
import '../../public/js/ace.js';
import '../../public/js/mode-php.js';
import '../../public/js/mode-javascript.js';
import '../../public/js/mode-c_cpp.js';
import '../../public/js/theme-monokai.js';
import '../../public/js/worker-php.js';

export default {
  data() {
    return {
      selectedLanguage: 'c',
      editor: null,
      output: '',
    };
  },
  mounted() {
    this.editor = ace.edit('editor');
    this.editor.setTheme('ace/theme/monokai');
    this.changeLanguage();
  },
  methods: {
    changeLanguage() {
      const language = this.selectedLanguage;

      if (language === 'c' || language === 'cpp') this.editor.session.setMode('ace/mode/c_cpp');
      else if (language === 'php') this.editor.session.setMode('ace/mode/php');
      else if (language === 'python') this.editor.session.setMode('ace/mode/python');
      else if (language === 'node') this.editor.session.setMode('ace/mode/javascript');
    },
    executeCode() {
      const language = this.selectedLanguage;
      const code = this.editor.getSession().getValue();

      // Simulasikan eksekusi kode secara lokal
      this.output = `Simulated output for ${language}: ${code}`;
    },
  },
};
</script>

<style>
.header {
  background: #000000;
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: white;
  padding: 10px;
  font-family: sans-serif;
  text-indent: -90px;
}

.control-panel {
  text-align: right;
  padding: 8px;
  font-family: sans-serif;
  font-size: 20px;
  background: #000000;
  font-weight: bold;
  color: white;
}

.languages {
  padding: 5px;
  border-radius: 5px;
}

.editor {
  height: 400px;
  width: 47%;
  float: left;
  background: #252525;
}

.button-container {
  clear: both;
}

.btn {
  background: #000;
  color: white;
  padding: 10px 15px;
  margin: 10px;
  border-radius: 5px;
  border: 0;
  float: right;
}

.output {
  width: 53%;
  resize: none;
  height: 400px;
  background: #252525;
  color: white;
  font-family: "Consolas", monospace;
  font-size: 12.5px;
  float: right;
}

.ace_active-line {
  width: 99%;
  background-color: black;
}
</style>
