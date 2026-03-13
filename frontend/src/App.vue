<template>
  <div class="layout-container" :class="{ 'auth-layout': isAuthPage }">
    <aside v-if="!isAuthPage" class="sidebar">
      <div class="logo">
        <h2 style="color: var(--accent-gold);">TemplePlatform</h2>
      </div>
      
      <nav class="nav-links">
        <router-link to="/" class="nav-item" active-class="active">
          <LayoutDashboard :size="20" />
          Dashboard
        </router-link>
        <router-link to="/temples" class="nav-item" active-class="active">
          <MapPin :size="20" />
          Temples
        </router-link>
        <router-link to="/darshan" class="nav-item" active-class="active">
          <Calendar :size="20" />
          Darshan
        </router-link>
        <router-link to="/pooja" class="nav-item" active-class="active">
          <Utensils :size="20" />
          Pooja
        </router-link>
        <router-link to="/donations" class="nav-item" active-class="active">
          <Heart :size="20" />
          Donations
        </router-link>
        <router-link to="/volunteers" class="nav-item" active-class="active">
          <Users :size="20" />
          Volunteers
        </router-link>
      </nav>

      <div style="margin-top: auto;">
        <div class="glass-card" style="padding: 1rem;">
          <p style="font-size: 0.8rem; color: var(--text-secondary);">Logged in as</p>
          <p style="font-weight: 600;">Admin User</p>
        </div>
      </div>
    </aside>

    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { 
  LayoutDashboard, MapPin, Calendar, Utensils, 
  Heart, Users 
} from 'lucide-vue-next'

const route = useRoute();
const isAuthPage = computed(() => route.path === '/login');
</script>

<style scoped>
.logo {
  padding: 0 1rem;
}
.nav-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
