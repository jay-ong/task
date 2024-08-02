'use client';
import { FormEvent, useState, useEffect } from "react";

const API_URL = 'http://localhost:8000'

export default function Home() {
  // let data: any = []
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');
  const [option, setOption] = useState([]);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const title = formData.get('search_title')
    const source = formData.get('search_source')

    const res = await fetch(`${API_URL}/scraper/api/movies?title=${title}&source=${source}`, {
      mode: 'cors',
      method: 'GET'
    });
    if (!res.ok) {
      setError(`Error: ${res.status} ${res.statusText}`);
      setResults([]);
      return;
    } else {
      setError('')
    }
    const data = await res.json()
    setResults(data)
  }

  async function get() {
    const res = await fetch(`${API_URL}/scraper/api/sources`, {
      mode: 'cors',
      method: 'GET'
    });
    const data = await res.json()
    setOption(data)
  }

  useEffect(() => {
    get()
  }, [])

  return (
    <main>
      <div className="lg:flex lg:items-center lg:justify-between bg-slate-200 p-6">
        <div className="min-w-0 flex-1">
          <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">
            Film Extractor
          </h2>
        </div>
      </div>
      <form onSubmit={onSubmit}>
        <div className="grid grid-cols-4 grid-flow-col gap-4 p-6">
          <div>
            <label className="block">
              <input name="search_title" type="text" placeholder="Search TV or File" className="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
                focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
              "/>
            </label>
          </div>
          <div>
            <select name="search_source" className="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
                focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
            ">
              <option value="">All Sites</option>
              {option.map((i, idx)=> (
                <option key={'option'+ idx} value={i}>{i}</option>
              ))}
            </select>
          </div>
          <div>
            <button type="submit" className="rounded mt-1 block px-3 py-2 text-white bg-sky-500 hover:bg-sky-700">
              Search
            </button>
          </div>
        </div>
      </form>
      {error.length > 0 &&
        (<div className="text-red-300">
        {error}
      </div>)
      }
      <div className="p-6">
        <div className="grid grid-cols-3 grid-flow-row gap-2 p-6">
          {results.map((item: any, index) => (
            <div key={index} className="mb-6">
              <img src={item.poster} className="w-c200"/>
              <h3>{item.title}</h3>
              <a href={item.endpoint+item.link_title} className="text-blue-500">{item.link_title}</a><br />
              <b>{item.tags}</b>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
