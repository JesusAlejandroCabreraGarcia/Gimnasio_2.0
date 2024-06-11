import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/Login.vue'
import RegisterUserVieww from './../components/RegisterUser.vue'
import DashboardView from '@/components/Dashboard.vue'
import HomeView from '@/components/Home.vue'
import AreasView from '@/components/Areas.vue'
import EmpleadoView from '@/components/Empleado.vue'
import HorarioView from '@/components/Horario.vue'
import InstructoresView from '@/components/Instructores.vue'
import PuestoView from '@/components/Puesto.vue'
import PersonaView from '@/components/Persona.vue'
import UsuarioView from '@/components/Usuario.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserVieww
    },
    
    {
      path: '/usuario',
      name: 'usuario',
      component: UsuarioView
    },
    {
      path: '/persona',
      name: 'persona',
      component: PersonaView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children:[
        {path:'/personas', name:'personas', component:RegisterUserVieww},
        {path:'/Home', name:'home', component:HomeView},
        {path:'/Areas', name:'areas', component:AreasView},
        {path:'/Empleado', name:'empleado', component:EmpleadoView},
        {path:'/Horario', name:'horario', component:HorarioView},
        {path:'/Instructores', name:'instructores', component:InstructoresView},
        {path:'/Puesto', name:'puesto', component:PuestoView},
      ]
    }
  ]
})

export default router
