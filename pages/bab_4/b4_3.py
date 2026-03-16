import streamlit as st

html_code = """
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"></script>
<script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest"></script>

<div>Teachable Machine Model</div>
<button onclick="init()">Start</button>
<div id="label-container"></div>

<script type="text/javascript">
    const URL = "PASTE_LINK_MODEL_KAMU/";

    let model, webcam, labelContainer, maxPredictions;

    async function init() {
        model = await tmImage.load(URL + "model.json", URL + "metadata.json");
        maxPredictions = model.getTotalClasses();
        alert("Model Loaded!");
    }
</script>
"""

st.components.v1.html(html_code, height=500)