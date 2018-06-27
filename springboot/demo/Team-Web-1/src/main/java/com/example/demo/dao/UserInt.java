package com.example.demo.dao;

import model.Users;

/**
 * dao文件夹下只提供接口，增删改查接口。
 * 
 * @author xx
 *
 */

public interface UserInt extends Maindao{

	public Users findByname(String name);
	
}
