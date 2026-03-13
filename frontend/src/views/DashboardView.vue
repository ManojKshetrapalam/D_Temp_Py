<template>
  <header style="margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <h1 class="fade-in">Dashboard Overview</h1>
      <p class="text-secondary">Welcome back to the Temple Management System</p>
    </div>
    <button class="btn-primary">
      <Plus :size="18" />
      Add Temple
    </button>
  </header>

  <div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
    <div class="glass-card fade-in">
      <p class="text-secondary">Total Bookings</p>
      <h2 style="font-size: 2rem; margin: 0.5rem 0;">{{ stats.total_bookings }}</h2>
      <span style="color: #10b981; font-size: 0.9rem;">+12% from last week</span>
    </div>
    <div class="glass-card fade-in" style="animation-delay: 0.1s;">
      <p class="text-secondary">Active Temples</p>
      <h2 style="font-size: 2rem; margin: 0.5rem 0;">{{ stats.active_temples }}</h2>
      <span style="color: var(--text-muted); font-size: 0.9rem;">No changes</span>
    </div>
    <div class="glass-card fade-in" style="animation-delay: 0.2s;">
      <p class="text-secondary">Total Donations</p>
      <h2 style="font-size: 2rem; margin: 0.5rem 0;">{{ stats.total_donations }}</h2>
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
          <tr v-for="booking in stats.recent_bookings" :key="booking.id" style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 1rem;">{{ booking.devotee }}</td>
            <td style="padding: 1rem;">{{ booking.temple }}</td>
            <td style="padding: 1rem;">{{ booking.date_time }}</td>
            <td style="padding: 1rem;">
              <span :class="getStatusClass(booking.status)">{{ booking.status }}</span>
            </td>
          </tr>
          <tr v-if="stats.recent_bookings.length === 0">
            <td colspan="4" style="padding: 2rem; text-align: center; color: var(--text-muted);">
              No recent bookings found.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Plus } from 'lucide-vue-next';
import api from '../services/api';

const stats = ref({
  total_bookings: '0',
  active_temples: 0,
  total_donations: '₹0',
  recent_bookings: [] as any[]
});

const fetchStats = async () => {
  try {
    const response = await api.get('dashboard-stats/');
    stats.value = response.data;
  } catch (error) {
    console.error('Error fetching dashboard stats:', error);
  }
};

const getStatusClass = (status: string) => {
  const base = 'status-tag ';
  if (status.toLowerCase() === 'confirmed') return base + 'status-confirmed';
  if (status.toLowerCase() === 'cancelled') return base + 'status-cancelled';
  return base + 'status-pending';
};

onMounted(() => {
  fetchStats();
});
</script>

<style scoped>
.text-secondary {
  color: var(--text-secondary);
}
.status-tag {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
}
.status-confirmed {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}
.status-cancelled {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}
.status-pending {
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}
</style>
