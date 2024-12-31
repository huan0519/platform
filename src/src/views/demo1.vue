<template>
  <div id="app">
    <div class="radio-inputs">
      <label class="radio">
        <input type="radio" name="radio" checked="" />
        <span class="name">处理前</span>
      </label>
      <label class="radio">
        <input type="radio" name="radio" />
        <span class="name">处理后</span>
      </label>
    </div>
  </div>
</template>

<script>

</script>

<style>
.radio-inputs {
  position: relative;
  display: flex;
  border-radius: 0.5rem;
  background-color: #70c489;
  box-sizing: border-box;
  font-size: 14px;
  width: 100%;
  padding: 1rem 1rem 0 1rem;
}

.radio-inputs .radio input {
  display: none;
}

.radio-inputs .radio .name {
  display: flex;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
  border: none;
  padding: 0.5rem 0.8rem;
  transition: all 0.15s ease-in-out;
  position: relative;
}

.radio-inputs .radio input:checked + .name {
  background-color: white;
  font-weight: 600;
}

.radio-inputs .radio input + .name:hover {
  color: white;
}

.radio-inputs .radio input:checked + .name:hover {
  color: #1d1d29;
}

.radio-inputs .radio input:checked + .name::after,
.radio-inputs .radio input:checked + .name::before {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: #70c489;
  bottom: 0;
}

.radio-inputs .radio input:checked + .name::after {
  right: -10px;
  border-bottom-left-radius: 300px;
  box-shadow: -3px 3px 0px 3px white;
}

.radio-inputs .radio input:checked + .name::before {
  left: -10px;
  border-bottom-right-radius: 300px;
  box-shadow: 3px 3px 0px 3px white;
}

</style>