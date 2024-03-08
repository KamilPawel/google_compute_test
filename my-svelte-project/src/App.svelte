<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';
  import Contact from './routes/Contact.svelte';
  import NotFound from './routes/NotFound.svelte';

  let routes = {
    '/': Home,
    '/contact': Contact,
    '*': NotFound
  };
</script>

<main>
  <Router {routes} />
</main>
