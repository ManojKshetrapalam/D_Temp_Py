<template>
  <div class="login-page" :style="{ backgroundImage: `url(${bgImage})` }">
    <div class="overlay"></div>
    
    <div class="login-container">
      <div class="glass-card login-card">
        <div class="brand">
          <h1 class="logo-text">Temple<span>Platform</span></h1>
          <p class="subtitle">Enter credentials to access temple management</p>
        </div>

        <form @submit.prevent="handleLogin" class="login-form">
          <div class="form-group">
            <label for="username">Admin ID</label>
            <div class="input-wrapper">
              <i class="lucide-user"></i>
              <input 
                type="text" 
                id="username" 
                v-model="username" 
                placeholder="Enter admin ID"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label for="password">Access Key</label>
            <div class="input-wrapper">
              <i class="lucide-lock"></i>
              <input 
                type="password" 
                id="password" 
                v-model="password" 
                placeholder="••••••••"
                required
              />
            </div>
          </div>

          <div class="form-options">
            <label class="checkbox-container">
              <input type="checkbox" v-model="rememberMe">
              <span class="checkmark"></span>
              Remember access
            </label>
            <a href="#" class="forgot-link">Forgot Access?</a>
          </div>

          <button type="submit" class="btn-primary login-btn" :disabled="loading">
            <span v-if="!loading">Initialize Session</span>
            <span v-else class="loader"></span>
          </button>
        </form>

        <div class="footer">
          <p class="security-text">By logging in, you agree to the <a href="#">Temple IT Security Protocol</a></p>
          <div class="version-info">
            <span>© 2024 Durgadevi Temple Management Systems</span>
            <span>Ver 2.4.0 (Devotional Cloud Integration)</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import bgImage from '../assets/login-bg.png';

const router = useRouter();
const username = ref('');
const password = ref('');
const rememberMe = ref(false);
const loading = ref(false);

const handleLogin = async () => {
  loading.value = true;
  // Mock login delay
  setTimeout(() => {
    loading.value = false;
    router.push('/');
  }, 1500);
};
</script>

<style scoped>
.login-page {
  height: 100vh;
  width: 100vw;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(10, 10, 12, 0.4) 0%, rgba(10, 10, 12, 0.9) 100%);
  z-index: 1;
}

.login-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 450px;
  padding: 1.5rem;
}

.login-card {
  padding: 3rem;
  border: 1px solid rgba(251, 191, 36, 0.3);
  animation: fadeInDown 0.8s ease-out;
}

.brand {
  text-align: center;
  margin-bottom: 2.5rem;
}

.logo-text {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--accent-gold);
  letter-spacing: -1px;
  margin-bottom: 0.5rem;
}

.logo-text span {
  color: #fff;
  font-weight: 300;
}

.subtitle {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.form-group label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-primary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.input-wrapper {
  position: relative;
}

.input-wrapper i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--accent-gold);
  font-size: 1.1rem;
}

.input-wrapper input {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 3rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  color: #fff;
  transition: var(--transition);
}

.input-wrapper input:focus {
  border-color: var(--accent-gold);
  background: rgba(255, 255, 255, 0.08);
  outline: none;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
}

.checkbox-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  color: var(--text-secondary);
}

.forgot-link {
  color: var(--accent-gold);
  text-decoration: none;
}

.login-btn {
  margin-top: 1rem;
  padding: 1rem;
  font-weight: 700;
  letter-spacing: 1px;
}

.footer {
  margin-top: 2.5rem;
  text-align: center;
  font-size: 0.75rem;
  color: var(--text-muted);
}

.security-text {
  margin-bottom: 1.5rem;
}

.security-text a {
  color: var(--text-secondary);
  text-decoration: underline;
}

.version-info {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.loader {
  width: 20px;
  height: 20px;
  border: 2px solid #000;
  border-bottom-color: transparent;
  border-radius: 50%;
  display: inline-block;
  animation: rotation 1s linear infinite;
}

@keyframes rotation {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
