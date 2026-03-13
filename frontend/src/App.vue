<template>
  <div class="layout-container">
    <aside class="sidebar">
      <div class="logo">
        <h2 style="color: var(--accent-gold);">TemplePlatform</h2>
      </div>
      
      <nav class="nav-links">
        <a href="#" class="nav-item active">
          <component :is="LayoutDashboard" :size="20" />
          Dashboard
        </a>
        <a href="#" class="nav-item">
          <component :is="MapPin" :size="20" />
          Temples
        </a>
        <a href="#" class="nav-item">
          <component :is="Calendar" :size="20" />
          Darshan
        </a>
        <a href="#" class="nav-item">
          <component :is="Utensils" :size="20" />
          Pooja
        </a>
        <a href="#" class="nav-item">
          <component :is="Heart" :size="20" />
          Donations
        </a>
        <a href="#" class="nav-item">
          <component :is="Users" :size="20" />
          Volunteers
        </a>
      </nav>

      <div style="margin-top: auto;">
        <div class="glass-card" style="padding: 1rem;">
          <p style="font-size: 0.8rem; color: var(--text-secondary);">Logged in as</p>
          <p style="font-weight: 600;">Admin User</p>
        </div>
      </div>
    </aside>

    <main class="main-content">
      <header style="margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center;">
        <div>
          <h1 class="fade-in">Dashboard Overview</h1>
          <p class="text-secondary">Welcome back to the Temple Management System</p>
        </div>
        <button class="btn-primary">
          <component :is="Plus" :size="18" />
          Add Temple
        </button>
      </header>

      <div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
        <div class="glass-card fade-in">
          <p class="text-secondary">Total Bookings</p>
          <h2 style="font-size: 2rem; margin: 0.5rem 0;">1,284</h2>
          <span style="color: #10b981; font-size: 0.9rem;">+12% from last week</span>
        </div>
        <div class="glass-card fade-in" style="animation-delay: 0.1s;">
          <p class="text-secondary">Active Temples</p>
          <h2 style="font-size: 2rem; margin: 0.5rem 0;">24</h2>
          <span style="color: var(--text-muted); font-size: 0.9rem;">No changes</span>
        </div>
        <div class="glass-card fade-in" style="animation-delay: 0.2s;">
          <p class="text-secondary">Total Donations</p>
          <h2 style="font-size: 2rem; margin: 0.5rem 0;">₹45,200</h2>
          <span style="color: #10b981; font-size: 0.9rem;">+24% this month</span>
        </div>
      </div>

      <section style="margin-top: 3rem;">
        <h3 style="margin-bottom: 1.5rem;">Recent Darshan Bookings</h3>
        <div class="glass-card" style="padding: 0;">
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="text-align: left; border-bottom: 1px solid var(--border-color);">
                <th style="padding: 1rem;">Devotee</th>
                <th style="padding: 1rem;">Temple</th>
                <th style="padding: 1rem;">Date/Time</th>
                <th style="padding: 1rem;">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="i in 5" :key="i" style="border-bottom: 1px solid var(--border-color);">
                <td style="padding: 1rem;">John Doe</td>
                <td style="padding: 1rem;">Somnath Temple</td>
                <td style="padding: 1rem;">Oct 12, 10:30 AM</td>
                <td style="padding: 1rem;">
                  <span style="background: rgba(16, 185, 129, 0.1); color: #10b981; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.8rem;">Confirmed</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { 
  LayoutDashboard, MapPin, Calendar, Utensils, 
  Heart, Users, Plus 
} from 'lucide-vue-next'
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
.text-secondary {
  color: var(--text-secondary);
}
</style>
