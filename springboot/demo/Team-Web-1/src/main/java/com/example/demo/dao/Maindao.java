package com.example.demo.dao;

public interface Maindao {
	
	public Object findAll();
	
	public <T>String Add(T a);
	
	public String deleteByName(String name);
	

}
