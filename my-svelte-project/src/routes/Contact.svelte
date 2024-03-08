<script>
  import BasePage from '../components/BasePage.svelte';

  let firstName = '';
  let lastName = '';
  let email = '';
  let phoneNumber = '';
  let message = '';
  let resMessage = {};

  const submitForm = async () => {
    const payload = { firstName, lastName, email, phoneNumber, message };

    // Replace 'https://api.example.com/submit-form' with your actual API endpoint
    const response = await fetch('http://localhost:8001/api/contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      // Handle success response
      resMessage = await response.json();
      firstName = '';
      lastName = '';
      email = '';
      phoneNumber = '';
      message = '';
    } else {
      // Handle error response
      console.error('Form submission failed');
    }
  };
</script>

<BasePage>
  <section class="bg-white dark:bg-green-900">
    <div class="max-w-screen-xl px-4 py-8 mx-auto lg:px-6 sm:py-16 lg:py-24">
      <div
        class="grid grid-cols-1 gap-6 text-center sm:gap-16 sm:grid-cols-2 lg:grid-cols-3"
      >
        <div>
          <div
            class="inline-flex items-center justify-center w-16 h-16 mx-auto text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-white"
          >
            <svg
              aria-hidden="true"
              class="w-10 h-10"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
                clip-rule="evenodd"
              />
            </svg>
          </div>
          <div class="mt-4">
            <h3 class="text-xl font-bold text-green-900 dark:text-white">
              Company information:
            </h3>
            <p
              class="mt-1 text-base font-normal text-green-500 dark:text-green-400"
            >
              Flowbite LLC<br />Tax id: USXXXXXX
            </p>
          </div>
        </div>

        <div>
          <div
            class="inline-flex items-center justify-center w-16 h-16 mx-auto text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-white"
          >
            <svg
              aria-hidden="true"
              class="w-10 h-10"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                clip-rule="evenodd"
              />
            </svg>
          </div>
          <div class="mt-4">
            <h3 class="text-xl font-bold text-green-900 dark:text-white">
              Address:
            </h3>
            <p
              class="mt-1 text-base font-normal text-green-500 dark:text-green-400"
            >
              SILVER LAKE, United States<br />1941 Late Avenue<br />Zip
              Code/Postal code: 03875
            </p>
          </div>
        </div>

        <div class="hidden lg:block">
          <div
            class="inline-flex items-center justify-center w-16 h-16 mx-auto text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-white"
          >
            <svg
              aria-hidden="true"
              class="w-10 h-10"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"
              />
            </svg>
          </div>
          <div class="mt-4">
            <h3 class="text-xl font-bold text-green-900 dark:text-white">
              Contact us:
            </h3>
            <p
              class="mt-1 text-base font-normal text-green-500 dark:text-green-400"
            >
              Email us for general queries, including marketing and partnership
              opportunities.
            </p>
            <a
              href="#"
              title=""
              class="block mt-1 text-base font-semibold text-green-900 dark:text-white hover:underline"
            >
              hello@flowbite.com
            </a>
          </div>
        </div>
      </div>

      <div class="max-w-3xl mx-auto mt-8 lg:mt-24">
        <form
          on:submit|preventDefault={submitForm}
          class="grid max-w-screen-md grid-cols-1 mx-auto gap-x-8 gap-y-6 sm:grid-cols-1"
        >
          <div>
            <label class="block mb-2 text-sm font-medium text-green-500"
              >{resMessage.message ? resMessage.message : ''}</label
            >
          </div>
          <div>
            <label
              for="first-name"
              class="block mb-2 text-sm font-medium text-green-900 dark:text-green-300"
              >First name</label
            >
            <input
              type="text"
              id="first-name"
              bind:value={firstName}
              class="block w-full p-3 text-sm text-green-900 border border-green-300 rounded-lg shadow-sm bg-green-50 focus:ring-green-500 focus:border-green-500 dark:bg-green-700 dark:border-green-600 dark:placeholder-green-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500 dark:shadow-sm-light"
            />
          </div>

          <div>
            <label
              for="last-name"
              class="block mb-2 text-sm font-medium text-green-900 dark:text-green-300"
              >Last name</label
            >
            <input
              type="text"
              id="last-name"
              bind:value={lastName}
              class="block w-full p-3 text-sm text-green-900 border border-green-300 rounded-lg shadow-sm bg-green-50 focus:ring-green-500 focus:border-green-500 dark:bg-green-700 dark:border-green-600 dark:placeholder-green-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500 dark:shadow-sm-light"
            />
          </div>

          <div>
            <label
              for="email"
              class="block mb-2 text-sm font-medium text-green-900 dark:text-green-300"
              >Your email</label
            >
            <input
              type="email"
              id="email"
              bind:value={email}
              class="shadow-sm bg-green-50 border border-green-300 text-green-900 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-green-700 dark:border-green-600 dark:placeholder-green-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500 dark:shadow-sm-light"
              required
            />
          </div>

          <div>
            <label
              for="phone-number"
              class="block mb-2 text-sm font-medium text-green-900 dark:text-green-300"
              >Phone number</label
            >
            <input
              type="text"
              id="phone-number"
              bind:value={phoneNumber}
              class="block w-full p-3 text-sm text-green-900 border border-green-300 rounded-lg shadow-sm bg-green-50 focus:ring-green-500 focus:border-green-500 dark:bg-green-700 dark:border-green-600 dark:placeholder-green-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500 dark:shadow-sm-light"
            />
          </div>

          <div class="sm:col-span-2 md:col-span-12">
            <label
              for="message"
              class="block mb-2 text-sm font-medium text-green-900 dark:text-green-400"
              >Your message</label
            >
            <textarea
              id="message"
              rows="6"
              bind:value={message}
              class="block p-2.5 w-full text-sm text-green-900 bg-green-50 rounded-lg shadow-sm border border-green-300 focus:ring-green-500 focus:border-green-500 dark:bg-green-700 dark:border-green-600 dark:placeholder-green-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500"
              placeholder=""
            ></textarea>
          </div>

          <button
            type="submit"
            class="px-5 py-3 text-sm font-medium text-center text-white rounded-lg bg-green-700 sm:w-fit hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
          >
            Send message
          </button>
        </form>
      </div>
    </div>
  </section>
</BasePage>
