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
      <div class="card"></div>
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


.card {
  width: 200px;
  height: 250px;
  border: none;
  border-radius: 10px;
  background: radial-gradient(ellipse farthest-side at 76% 77%, rgba(245, 228, 212, 0.25) 4%, rgba(255, 255, 255, 0) calc(4% + 1px)), radial-gradient(circle at 76% 40%, #fef6ec 4%, rgba(255, 255, 255, 0) 4.18%), linear-gradient(135deg, #ff0000 0%, #000036 100%), radial-gradient(ellipse at 28% 0%, #ffcfac 0%, rgba(98, 149, 144, 0.5) 100%), linear-gradient(180deg, #cd6e8a 0%, #f5eab0 69%, #d6c8a2 70%, #a2758d 100%);
  background-blend-mode: normal, normal, screen, overlay, normal;
  box-shadow: 0px 0px 10px 1px #000000;
}


</style>