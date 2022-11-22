import Head from 'next/head';
import React, { useState, useEffect } from 'react';

interface User {
	id: string;
	firstName: string;
	lastName: string;
	email: string;
	password: string;
}

export default function Users() {
	const [firstName, setFirstName] = useState<string>('');
	const [lastName, setLastName] = useState<string>('');
	const [email, setEmail] = useState<string>('');
	const [password, setPassword] = useState<string>('');
	const [users, setUsers] = useState<Array<User>>([]);

	useEffect(() => {
		async function fetchUsers() {
			const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/user/`);
			const json = await res.json();
			console.log(json);
			setUsers(json);
		}
		fetchUsers();
	}, []);

	function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
		const { id, value } = e.target;
		if (id === 'firstName') setFirstName(value);
		if (id === 'lastName') setLastName(value);
		if (id === 'email') setEmail(value);
		if (id === 'password') setPassword(value);
	}

	async function handleSubmit() {
		const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/user/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				firstName,
				lastName,
				email,
				password,
			}),
		});
		const json = await res.json();
		setUsers([...users, json]);
	}

	return (
		<div>
			<Head>
				<title>Notes</title>
			</Head>
			<div className='container p-10 m-10 mx-auto'>
				<div className='flex flex-col'>
					<h1 className='mb-3 font-bold'>Users</h1>
					<label>
						First Name
						<input id='firstName' value={firstName} onChange={handleChange} className='border-2' />
					</label>
					<label>
						Last Name
						<input id='lastName' value={lastName} onChange={handleChange} className='border-2' />
					</label>
					<label>
						Email
						<input id='email' value={email} onChange={handleChange} className='border-2' />
					</label>
					<label>
						Password
						<input id='password' value={password} onChange={handleChange} className='border-2' />
					</label>
					<div className='p-3 m-5 mx-auto'>
						<button onClick={handleSubmit} className='p-3 text-white bg-green-500'>
							Submit
						</button>
					</div>
					<div>
						<ul>
							{users &&
								users.map((user) => (
									<li key={user.id} className='p-3 m-3 bg-yellow-100 border-2 border-yellow-200'>
										{user.firstName} {user.lastName} - {user.email}
									</li>
								))}
						</ul>
					</div>
				</div>
			</div>
		</div>
	);
}
