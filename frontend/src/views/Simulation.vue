<template>
  <div>
    <h2>Simulazione Quantistica</h2>
    <button @click="runSimulation">Avvia</button>
    <div v-for="(msg, index) in messages" :key="index">{{ msg }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return { messages: [] };
  },
  methods: {
    runSimulation() {
      const socket = new WebSocket("ws://localhost:5000/ws/simulation");
      socket.onmessage = (event) => this.messages.push(event.data);
    }
  }
};
</script>